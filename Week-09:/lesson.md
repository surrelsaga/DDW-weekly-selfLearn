## Technically, the lesson is simple it's just working with data (1D, 2D-table) and higher-dimensional data (neural networks)

`Pandas`: to read csv, spreadsheet -> mostly to operate with tabular data (2D)

`Numpy`: pandas is based on numpy arrays. numpy can handle higher dimensional data

1\. One important thing, to extract an axis (or element) from the data in pandas, numpy

pandas: `df.loc[arg1, arg2, ...]`, `df.iloc[arg1, arg2, ...]` => have slicing. .loc is INCLUSIVE of the end, .iloc is EXCLUSIVE
difference: loc works by name (labels), iloc works by integer position

numpy: `array[arg1, arg2, ...]` => have slicing and is EXCLUSIVE (same as python slicing, same as iloc)
watch out: only `.loc` is inclusive. everything else (`.iloc`, numpy) drops the end index
note: `array[...]` (square brackets) is indexing. `np.array([...])` is the constructor that builds an array from a list -> don't mix them up

=> main idea: the args are just "axis"s (row/column in 2D, vectors in multi-dimensions) and the result of these function calls
are just the INTERSECTION of these axes

quick examples (HDB dataset, row = a sale, columns = town/block/resale_price/...):

pandas .loc (by label, end INCLUSIVE):
- e.g: `df.loc[:, 'resale_price']`  => all rows, 1 column -> Series
- e.g: `df.loc[0, :]`  => first row, all columns -> Series
- e.g: `df.loc[0:9, :]`  => rows 0..9 = 10 rows (9 is INCLUDED)
- e.g: `df.loc[:, ['town','block','resale_price']]`  => pick specific columns
- e.g: `df.loc[df['resale_price'] > 500_000, columns]`  => condition = boolean filter on rows

pandas .iloc (by position, end EXCLUSIVE):
- e.g: `df.iloc[0:10, [1, 3, -1]]`  => rows 0..9 = 10 rows, columns by position

numpy (by position, end EXCLUSIVE):
- e.g: `array[0]` or `array[0, :]`  => first row
- e.g: `array[:, 0]`  => first column
- e.g: `array[0, 1]`  => single element (row 0, col 1)
- e.g: `array[:10, 1:3]`  => first 10 rows, columns 1 & 2 (col 3 dropped)

careful: for reduction functions (`sum`, `mean`, `std`) the `axis` arg means the OPPOSITE of what you'd guess
`axis=0` => collapses DOWN the rows => you get one value PER COLUMN
`axis=1` => collapses across columns => you get one value PER ROW

2\. Normalization (they make you write these functions in the pset)

we rescale columns because features have different scales (e.g. floor_area 33-249 vs lease_year 1966-2019)

z-norm (standardization): `(data - mean) / std` => mean becomes 0, std becomes 1
min-max: `(data - min) / (max - min)` => squashes everything into [0, 1]

also: split data into train/test (usually 70-80% train), and the split must be RANDOM to avoid systematic bias

3\. Other than that:
`matplotlib` and `seaborn`(sns) are used to visualize data (mostly the graphs I know)

relationship between variables: scatterplot, lineplot

distribution of one variable: histplot (histogram)

categorical comparison: boxplot, barplot

extra: `hue='column'` colours the plot by another column. boxplot outliers are capped at Q1 - 1.5*IQR and Q3 + 1.5*IQR (NOT the real min/max)
