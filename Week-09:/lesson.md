## Technically, the lesson is simple it's just working with data (1D, 2D-table) and higher-dimensional data (neural networks)

`Pandas`: to read csv, spreadsheet -> mostly to operate with tabular data (2D)

`Numpy`: pandas is based on numpy arrays. numpy can handle higher dimensional data

1\. One important method, to extract an axis (or element) from the data in pandas, numpy

pandas: .loc(arg1, arg2, ...), .iloc(arg1, arg2, arg3) => have slicing .loc is inclusive, .iloc is exclusive
difference: loc can work with rows/columns by calling their name (labels), iloc work by integer position

numpy: array(arg1, arg2,...) => have slicing and is inclusive

=> main idea: the args are just "axis"s (row/column in 2D, vectors in multi-dimensions) and the result of these function calls
are just the INTERSECTION of these axes

2\. Other than that:
`matplotlib` and `seaborn`(sns) are used to visualize data (mostly the graphs I know)

relationship between variables: scatterplot, lineplot

distribution of one variable: histplot (histogram)

categorical comparison: boxplot, barplot
