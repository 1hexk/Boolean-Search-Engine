# Boolean Search Engine


##  I. How to Use

- **How to Search**
the syntax for queries is defined as follows:

-   Space `" "` represents the OR operator. For example, `"apple ipad"` means `apple OR ipad`.
-   The "&" symbol with no spaces represents the AND operator. For example, `"apple&ipad"` means `apple AND ipad`.
-   The AND operator takes priority over the OR operator. For instance:
    -   `samsung sony&tv` translates to `samsung OR (sony AND tv)`.
    -   `samsung&sony tv` translates to `(samsung AND sony) OR tv`.

we assumed that the AND operator "&" will always appear with no spaces before or after it.

- **Parsing and Index Creating Time:**
![Time taken to run each on 209K+ documents.](https://ibb.co/RCLZxSR)

- **Sample Results:**
  | Query                | Number of Documents | Time to Search (microseconds) |
  |----------------------|---------------------|--------------------------------|
  | the                  | 144,195             | 4,568.49                       |
  | Trump Biden          | 12,180              | 437.29                         |
  | Healthy&Living       | 6,798               | 2,631.99                       |
  | Style Healthy&Living | 19,401              | 2,074.00                       |
  | Healthy&Living Style | 19,401              | 1,886.90                       |

## II. Design Explanation
- **Parsing:**
  - Save each line as a JSON object in an array.

- **Inverted Index:**
 is a dictionary that has each word and the ID's of all documents that contain that word.
 
  - Save the lowercase of each word to make searching easier (no need to match case words whn searching).
  - Example: `The` ↔ `the`, `World` ↔ `world`.
  
  - Links and any other word separated by punctuation (`-`, `'`, `"`, `.`, `,`, etc.) are saved as a whole to preserve the integrity of the words.
  
  - Example: `James M. Dorsey` → `M.` ≠ `M`, `U.S.` (United States) ≠ `US` (object pronoun).

- **Boolean Searching:**
  - **AND case:** Save the first word’s value then intersecting it with the rest of the words.
  - **OR case:** Add each word’s value to the Results list.
