# Sugar's Maria

Here's a brief overview of the functionalities provided by this class:

    Data Initialization:
        The start method is a convenient way 
        to load multiple data files with fallback options
        for manual path input, accommodating the common scenario 
        where data not in expected locations.

    Row Name Correction:
        Through row_names_fix, it offers a 
        flexible approach to rectify row names 
        based on either a typo correction or 
        column-based search, enhancing data 
        consistency for downstream analysis.

    Sublist Generation: 
        The sublists_ method provides a way 
        to chunk a list into sublists of 
        approximately equal size, 
        which can be useful in batch processing 
        or when dividing data for cross-validation purposes.

    Statistical Summary: 
        With stats_, you can quickly obtain 
        a comprehensive statistical summary 
        of a data subset, including quantiles,
        which are crucial for understanding 
        data distribution and variance.

    Array Conversion:
        The num_toarray method transforms dataframe columns 
        into numpy arrays, catering to scenarios
        where numerical operations are more efficiently handled 
        with NumPy's capabilities.

    Data Extraction: 
        Through simple_extract_, you facilitate the extraction of 
        specific columns from a dataframe, supporting scenarios
        where only a subset of the data is needed for analysis.

    Data Validation: 
        The validation_ method provides a mechanism to filter data 
        based on a differential condition, allowing for 
        the identification of significant changes or 
        anomalies within a dataset.

    Data Expansion: 
        With extract_, lists within dataframe cells can be 
        expanded into separate columns, aiding in 
        the normalization of data structures for analysis.

    PPG Signal Column Detection: 
        Lastly, simple_PPG_iloc_detector helps in 
        identifying columns related to photoplethysmogram (PPG) signals, 
        demonstrating the class's applicability to 
        specific biomedical signal processing tasks.

Each method is designed with static accessibility, ensuring that they can be utilized without the need to instantiate the class, thereby providing a straightforward interface for users to interact with their data.

# Example method usage
        import main
        import pandas as pd
        maria = main.Maria()
        data_frame = pd.read_excel("path_to_your_file.xlsx")
        fixed_data_frame = maria.row_names_fix(data_frame)
