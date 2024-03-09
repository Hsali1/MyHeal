This program restores the chunks that were created using mybreak: https://github.com/Hsali1/MyBreak

usage:
```
> myheal <source> <prefix> <chunk size (K)> <number of chunks>
```

usage example:
```
> python .\myheal.py Coffee.png Tester 10000 4
```

Assume we have 4 chunks of 10000 KB each, this program will merge those chunks back into a file called Coffee.png

Example Output:
```
Chunk 1 merged successfully.
Chunk 2 merged successfully.
Chunk 3 merged successfully.
Chunk 4 merged successfully.
All chunks merged successfully.
```