#        #          #                    In the name of God   #    #
#
#GitHub.com/cloner174
#cloner174.org@gmail.com
#
import pandas as pd
import numpy as np
import re

class Maria:
    @staticmethod
    def start(default=True):
        if default:
            data_paths = ['./data/data2.xlsx', './data/ppg_data_glu2hpp.xlsx', './data/ppg_data_fbs.xlsx']
            data = []
            for path in data_paths:
                try:
                    data.append(pd.read_excel(path))
                except FileNotFoundError:
                    input_path = input(f"Enter the path for {path.split('/')[-1]} found in the zip file: ")
                    try:
                        input_path = re.sub(r"\\", "/", input_path)
                        data.append(pd.read_excel(input_path))
                    except Exception as e:
                        raise ValueError(f"Invalid path provided for {path}. Error: {e}")
            return data
    
    @staticmethod
    def row_names_fix(df, describe_column=0, typo=None, fbs_ncol=None, glu_ncol=None):
        if typo:
            Maria.typo_fix(df, typo, describe_column)
        else:
            Maria.col_search_fix(df, describe_column, fbs_ncol, glu_ncol)
        return df
    
    @staticmethod
    def typo_fix(df, typo, describe_column):
        for i, row in df.iterrows():
            id_num = re.search(r'\d+', row[describe_column])
            id_str = id_num.group(0) if id_num else "00"
            df.at[i, describe_column] = f"{id_str}_{typo}"
    
    @staticmethod
    def col_search_fix(df, describe_column, fbs_ncol, glu_ncol):
        for i, row in df.iterrows():
            id_search = re.search(r'\d+', row[describe_column])
            id_num = id_search.group() if id_search else "00"
            sugar_type = 'glu' if 'glu' in row[describe_column].lower() else 'fbs'
            df.at[i, describe_column] = f"{id_num}_{sugar_type}"
            if fbs_ncol is not None and 'fbs' in sugar_type:
                try:
                    df.at[i, 'RealSugar'] = int(row[fbs_ncol])
                except ValueError:
                    pass  # Handle the case where conversion to int fails
            elif glu_ncol is not None and 'glu' in sugar_type:
                try:
                    df.at[i, 'RealSugar'] = int(row[glu_ncol])
                except ValueError:
                    pass  # Handle the case where conversion to int fails
    
    @staticmethod
    def sublists_(List_, n_):
        """
        Splits a list into n approximately equal-sized sublists.

        :param List_: The list to be split.
        :param n_: The desired number of sublists.
        :return: A list of sublists.
        """
        length = len(List_)
        avg = length / float(n_)
        sublists = [List_[int(last):int(last + avg)] for last in np.arange(0, length, avg)]
        return sublists
    
    @staticmethod
    def stats_(subset):
        quantiles = [0.2, 0.25, 0.27, 0.3, 0.33, 0.35, 0.36, 0.60, 0.61, 0.64, 0.66, 0.69, 0.72, 0.75, 0.95]
        return [
            np.mean(subset),
            np.median(subset),
            np.std(subset),
            np.var(subset),
            *[np.quantile(subset, q) for q in quantiles]
        ]
    
    @staticmethod
    def num_toarray(data_frame, ncol_start=1, ncol_end=None):
        col_names = list(data_frame.columns)
        ncol_end = ncol_end or data_frame.shape[1]
        data_array = np.array(data_frame)
        for i in range(data_array.shape[0]):
            for j in range(ncol_start, ncol_end):
                data_array[i, j] = np.array(data_array[i, j])
        return pd.DataFrame(data_array, columns=col_names)
    
    @staticmethod
    def simple_extract_(data_frame, ncol_start=1, ncol_end=None):
        ncol_end = ncol_end or data_frame.shape[1]
        extracted_data = [list(row[ncol_start:ncol_end]) for _, row in data_frame.iterrows()]
        extracted_array = np.array(extracted_data)
        return extracted_data, extracted_array
    
    @staticmethod
    def validation_(data_frame, prob=None, ncol_start=1, ncol_end=None):
        ncol_end = ncol_end or data_frame.shape[1]
        extracted_data = Maria.simple_extract_(data_frame, ncol_start, ncol_end)[0]
        results = []
        for row in extracted_data:
            row_results = []
            for cell in row:
                diffs = np.diff(cell)
                prob = prob or np.mean(diffs)
                valid_indices = np.where(diffs < prob)[0]
                row_results.append([cell[i] for i in valid_indices])
            results.append(row_results)
        return results, np.array(extracted_data)
    
    @staticmethod
    def extract_(data_frame):
        expanded_data = []
        for _, row in data_frame.iterrows():
            new_row = {}
            for col_name, cell_value in row.items():
                if isinstance(cell_value, list):
                    for index, value in enumerate(cell_value):
                        new_row[f'{col_name}_{index}'] = value
                else:
                    new_row[col_name] = cell_value
            expanded_data.append(new_row)
        return pd.DataFrame(expanded_data)
    
    @staticmethod
    def simple_PPG_iloc_detector(data_frame):
        col_indices = {'RGB': [], 'Red': [], 'RGdiff': [], 'LowpassRGB': [], 'LowpassRed': [], 'LowpassRGdiff': []}
        for i, col_name in enumerate(data_frame.columns):
            for key in col_indices.keys():
                if re.search(key, col_name, re.IGNORECASE):
                    col_indices[key].append(i)
        return tuple(col_indices.values())

#end#
