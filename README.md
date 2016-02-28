# Path Truncator

This script will cut off the ends of path components. I've had this kicking
around in my `fish_prompt` since forever, and I recently decided to clean it
up.

## Usage

**pathtrunc.py [-h] <path> <len>**

Truncates *path* to *len* characters.

This snippet will include it in a `fish_prompt`

```fish
echo -n (pathtrunc $PWD 25)
```

This one will include it in a bash `$PS1`

```bash
PS1="\$(~/bin/pathtrunc \$PWD 25)"
```
