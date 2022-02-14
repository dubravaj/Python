## High Performance Python notes (from book High Performance Python) 

<br/>

#### <b>List and tuples</b> 
- tuples - static arrays (immutable)
- list stores its size
- \_\_eq\_\_ and \_\_lt\_\_ for comparison of custom objects
- builtin <b>sort</b> method hybridizes insertion and merge sort algorithms
- <b>bisect</b> module
- Tuples are cached by the Python runtime, which means that we don’t need to talk
to the kernel to reserve memory every time we want to use one. 
- both list and tuple can take mixed types - this can introduce quite some overhead and reduce some potential optimizations
- <b>Lists</b>
    - when resizing from N, it allocates new array with size M > N (not N+1), for future appends
    - many small lists or large list can lead to increased allocation of memory that is not good - when using append operation (initial creation of list does not allocate extra space)
- <b>Tuples</b>
    - concatenation of tuples
    - no inplace-like operator, concatenatio always leads to usage of new location in memory
    - list will be larger in memory than tuple with the same data
    - for small tuples (1-20), when they are no longer in use, they are not immediately returned to OS, but they are saved for future use

#### <b>Dictionaries and Sets</b>

- a hashable type is one that implements both the \_\_hash\_\_ magic (still magic ?)
function and either \_\_eq\_\_ or \_\_cmp\_\_ . All native types in Python already implement these, and any user classes have default values

- insertion/lookup depends on hash function
- <b>probing</b> mechanism - computing index for insertion
- load factor - how well is data distributed through hash table, it is related to the entropy of the hash function
- similar procedure for search - computing index where the initial lookup will be done, if we hit , return, otherwise new indexes will be computed until hit or finding an empty bucket - key is not there
- <b>resizing</b>
    - table has to be resized as items are added
    - it can be shown that a table that is no more than two-thirds full will have optimal space savings
        - when table reaches this critical point, it is resized (more space, creation of new mask for computing index, reinsertion of elements)
    - It is important to note that resizing can happen to make a hash table larger or smaller.
    - resize is done only during insert
- By default, the smallest size of a dictionary or set is 8
- User-defined classes also have default hash and comparison functions. The default
\_\_hash\_\_ function simply returns the object’s placement in memory as given by the
built-in <b>id</b> function, similarly, the \_\_cmp\_\_ operator compares the numerical value of the object’s placement in memory.
- idea of “how well distributed my hash function is” is called the entropy of the hash function
- <b>Dictionaries and Namespaces</b>
    - locals() - list of local variables
    - globals() dictionary
    - \_\_builtin\_\_ object is search after lookup was unsucessful in locals and globals
    - importing functions from module will speed up the code - less lookups
    - local reference to global object could be helpfull if it is needed in a loop called many time

#### <b>Iterators and Generators</b>

- iterable object - has \_\_iter\_\_ method
- to make iterator from object - use <b>iter</b> builtin function
- generator is also an iterator
- <b>xrange</b> is a generator
- <b>range</b> - we need to allocate
a new list and precompute its values, and then we still must create an iterator
- <b>generator comprehension</b> - (\<value\> for \<item\> in \<sequence\> if \<condition\>)
- generators are ideal for infinite series
- <b>itertools</b> module 

#### <b>Matrix and Vector Computation</b>
- Python does not natively support vectorization
    - reasons: Python lists store pointers to the actual data, Python bytecode is not optimized for vectorization
- pointers in lists are source of a lot of performance degradation for matrix operations
- problem with data fragmentation in memory
- Von Neuman bottleneck - we cant transfer the data needed by CPU instantly
 - branch prediction and pipelining - try to predict the next instruction and load the relevant portions of memory into the cache while still working
on the current instruction
- linux <b>perf</b>
    - pipelining -  To get a better handle on this pipelining, stalled-
cycles-frontend and stalled-cycles-backend tell us how many cycles our program
was waiting for the frontend or backend of the pipeline to be filled
    - With pipelining, the CPU is able to run the current operation while fetching
and preparing the next one
- vectorization can be done only if we hve all necessary data in CPU cache (need to have data in a continuous memory block)
- <b>array</b> object stores data sequentially in the memory

- <b>numpy</b>
    - can efficiently vectorize operations
    - stores data in contiguous chunks of memory
    - e.g. numpy.dot is vectorized

    - operations e.g. <b>+=,*=</b> are done in-place, arr = arr + arr2 is not done in place
- <b>numexpr</b> module








