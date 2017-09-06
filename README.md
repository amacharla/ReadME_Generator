<h4 class="task">
    0. &gt;&gt;&gt; ht = {}
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1233">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that creates a hash table.</p><ul>
<li>Prototype: <code>hash_table_t *hash_table_create(unsigned long int size);</code>
<ul>
<li>where <code>size</code> is the size of the array</li>
</ul></li>
<li>Returns a pointer to the newly created hash table</li>
<li>If something went wrong, your function should return <code>NULL</code></li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 0-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;

    ht = hash_table_create(1024);
    printf("%p\n", (void *)ht);
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-hash_table_create.c -o a
julien@ubuntu:~/0x19. Hash tables$ ./a 
0x238a010
julien@ubuntu:~/0x19. Hash tables$ valgrind ./a
==7602== Memcheck, a memory error detector
==7602== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==7602== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==7602== Command: ./a
==7602== 
0x51fc040
==7602== 
==7602== HEAP SUMMARY:
==7602==     in use at exit: 8,208 bytes in 2 blocks
==7602==   total heap usage: 2 allocs, 0 frees, 8,208 bytes allocated
==7602== 
==7602== LEAK SUMMARY:
==7602==    definitely lost: 16 bytes in 1 blocks
==7602==    indirectly lost: 8,192 bytes in 1 blocks
==7602==      possibly lost: 0 bytes in 0 blocks
==7602==    still reachable: 0 bytes in 0 blocks
==7602==         suppressed: 0 bytes in 0 blocks
==7602== Rerun with --leak-check=full to see details of leaked memory
==7602== 
==7602== For counts of detected and suppressed errors, rerun with: -v
==7602== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x19. Hash tables$
</code></pre>

<h4 class="task">
    1. djb2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1234">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a hash function implementing the djb2 algorithm.</p><ul>
<li>Prototype: <code>unsigned long int hash_djb2(const unsigned char *str);</code></li>
<li>You are allowed to copy and paste the function from <a href="http://www.cse.yorku.ca/%7Eoz/hash.html">this page</a></li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 1-djb2.c 
unsigned long int hash_djb2(const unsigned char *str)
{
    unsigned long int hash;
    int c;

    hash = 5381;
    while ((c = *str++))
    {
        hash = ((hash &lt;&lt; 5) + hash) + c; /* hash * 33 + c */
    }
    return (hash);
}
julien@ubuntu:~/0x19. Hash tables$ 
julien@ubuntu:~/0x19. Hash tables$ cat 1-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    char *s;

    s = "cisfun";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    s = "Don't forget to tweet today";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    s = "98";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 1-main.c 1-djb2.c -o b
julien@ubuntu:~/0x19. Hash tables$ ./b 
6953392314605
3749890792216096085
5861846
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre>

<h4 class="task">
    2. key -&gt; index
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1235">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that gives you the index of a key.</p><ul>
<li>Prototype: <code>unsigned long int key_index(const unsigned char *key, unsigned long int size);</code>
<ul>
<li>where <code>key</code> is the key</li>
<li>and <code>size</code> is the size of the array of the hash table</li>
</ul></li>
<li>This function should use the <code>hash_djb2</code> function that you wrote earlier</li>
<li>Returns the index at which the key/value pair should be stored in the array of the hash table</li>
<li>You will have to use this hash function for all the next tasks</li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 2-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    char *s;
    unsigned long int hash_table_array_size;

    hash_table_array_size = 1024;
    s = "cisfun";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));
    s = "Don't forget to tweet today";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));
    s = "98";
    printf("%lu\n", hash_djb2((unsigned char *)s));
    printf("%lu\n", key_index((unsigned char *)s, hash_table_array_size));  
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 2-main.c 1-djb2.c 2-key_index.c -o c
julien@ubuntu:~/0x19. Hash tables$ ./c 
6953392314605
237
3749890792216096085
341
5861846
470
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre>

<h4 class="task">
    3. &gt;&gt;&gt; ht['betty'] = 'holberton'
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1236">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that adds an element to the hash table.</p><ul>
<li>Prototype: <code>int hash_table_set(hash_table_t *ht, const char *key, const char *value);</code>
<ul>
<li>Where <code>ht</code> is the hash table you want to add or update the key/value to</li>
<li><code>key</code> is the key. <code>key</code> can not be an empty string</li>
<li>and <code>value</code> is the value associated with the key. <code>value</code> can be an empty string</li>
</ul></li>
<li>Returns: <code>1</code> if it succeeded, <code>0</code> otherwise</li>
<li>In case of collision, add the new node at the beginning of the list</li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 3-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;

    ht = hash_table_create(1024);
    hash_table_set(ht, "betty", "holberton");
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre><p><em>Tip from <a href="https://twitter.com/JennieZChu">Jennie</a></em>: if you want to test for collisions, here are some strings that collide using the djb2 algorithm:</p><ul>
<li>hetairas collides with mentioner</li>
<li>heliotropes collides with neurospora</li>
<li>depravement collides with serafins</li>
<li>stylist collides with subgenera</li>
<li>joyful collides with synaphea</li>
<li>redescribed collides with urites</li>
<li>dram collides with vivency</li>
</ul>

<h4 class="task">
    4. &gt;&gt;&gt; ht['betty']
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1251">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that retrieves a value associated with a key.</p><ul>
<li>Prototype: <code>char *hash_table_get(const hash_table_t *ht, const char *key);</code>
<ul>
<li>where <code>ht</code> is the hash table you want to look into</li>
<li>and <code>key</code> is the key you are looking for</li>
</ul></li>
<li>Returns the value associated with the element, or <code>NULL</code> if <code>key</code> couldn't be found</li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 4-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;
    char *value;

    ht = hash_table_create(1024);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Jennie", "and Jay love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Holberton");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_set(ht, "c", "isfun");

    value = hash_table_get(ht, "python");
    printf("%s:%s\n", "python", value);
    value = hash_table_get(ht, "Jennie");
    printf("%s:%s\n", "Jennie", value);
    value = hash_table_get(ht, "N");
    printf("%s:%s\n", "N", value);
    value = hash_table_get(ht, "Asterix");
    printf("%s:%s\n", "Asterix", value);
    value = hash_table_get(ht, "Betty");
    printf("%s:%s\n", "Betty", value);
    value = hash_table_get(ht, "98");
    printf("%s:%s\n", "98", value);
    value = hash_table_get(ht, "c");
    printf("%s:%s\n", "c", value);
    value = hash_table_get(ht, "javascript");
    printf("%s:%s\n", "javascript", value);
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 4-main.c 0-hash_table_create.c 1-djb2.c 2-key_index.c 3-hash_table_set.c 4-hash_table_get.c -o e
julien@ubuntu:~/0x19. Hash tables$ ./e 
python:awesome
Jennie:and Jay love asm
N:queens
Asterix:Obelix
Betty:Holberton
98:Battery Street
c:isfun
javascript:(null)
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre>

<h4 class="task">
    5. &gt;&gt;&gt; print(ht)
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1252">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that prints a hash table.</p><ul>
<li>Prototype: <code>void hash_table_print(const hash_table_t *ht);</code>
<ul>
<li>where <code>ht</code> is the hash table</li>
</ul></li>
<li>You should print the key/value in the order that they appear in the array of hash table

<ul>
<li>Order: array, list</li>
</ul></li>
<li>Format: see example</li>
<li>If <code>ht</code> is NULL, don't print anything</li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 5-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;

    ht = hash_table_create(1024);
    hash_table_print(ht);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Jennie", "and Jay love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Holberton");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_print(ht);
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 5-main.c 0-hash_table_create.c 1-djb2.c 2-key_index.c 3-hash_table_set.c 4-hash_table_get.c 5-hash_table_print.c -o f
julien@ubuntu:~/0x19. Hash tables$ ./f 
{}
{'Betty': 'Holberton', 'python': 'awesome', 'Jennie': 'and Jay love asm', '98': 'Battery Street', 'N': 'queens', 'c': 'fun', 'Asterix': 'Obelix'}
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre>

<h4 class="task">
    6. &gt;&gt;&gt; del ht
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1388">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>Write a function that deletes a hash table.</p><ul>
<li>Prototype: <code>void hash_table_delete(hash_table_t *ht);</code>
<ul>
<li>where <code>ht</code> is the hash table</li>
</ul></li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 6-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;
    char *key;
    char *value;

    ht = hash_table_create(1024);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Jennie", "and Jay love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Holberton");
    hash_table_set(ht, "98", "Battery Streetz");
    key = strdup("Tim");
    value = strdup("Britton");
    hash_table_set(ht, key, value);
    key[0] = '\0';
    value[0] = '\0';
    free(key);
    free(value);
    hash_table_set(ht, "98", "Battery Street"); 
    hash_table_set(ht, "hetairas", "Jennie");
    hash_table_set(ht, "hetairas", "Jennie Z");
    hash_table_set(ht, "mentioner", "Jennie");
    hash_table_set(ht, "hetairas", "Jennie Z Chu");
    hash_table_print(ht);
    hash_table_delete(ht);
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 6-main.c 0-hash_table_create.c 1-djb2.c 2-key_index.c 3-hash_table_set.c 4-hash_table_get.c 5-hash_table_print.c 6-hash_table_delete.c -o g
julien@ubuntu:~/0x19. Hash tables$ valgrind ./g
==6621== Memcheck, a memory error detector
==6621== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==6621== Using Valgrind-3.10.1 and LibVEX; rerun with -h for copyright info
==6621== Command: ./g
==6621== 
{'Betty': 'Holberton', 'mentioner': 'Jennie', 'hetairas': 'Jennie Z Chu', 'python': 'awesome', 'Jennie': 'and Jay love asm', '98': 'Battery Street', 'N': 'queens', 'c': 'fun', 'Tim': 'Britton', 'Asterix': 'Obelix'}
==6621== 
==6621== HEAP SUMMARY:
==6621==     in use at exit: 0 bytes in 0 blocks
==6621==   total heap usage: 37 allocs, 37 frees, 8,646 bytes allocated
==6621== 
==6621== All heap blocks were freed -- no leaks are possible
==6621== 
==6621== For counts of detected and suppressed errors, rerun with: -v
==6621== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre>

<h4 class="task">
    7. $ht['Betty'] = 'Holberton'
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><div class="task_progress_score_bar" data-correction-id="12694" data-task-id="1253">
<div class="task_progress_bar">
<div class="task_score_bar">
</div>
</div>
<div class="task_progress_score_text">
        Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">completion score: 0%</span>)
      </div>
</div><p>In <a href="http://php.net/manual/en/intro-whatis.php">PHP</a>, hash tables are <strong>ordered</strong>. Wait... WAT? How is this even possible?</p><p><img src="https://media.giphy.com/media/IUp9WRHyCwUEg/giphy.gif"/><br>
<br/></br></p><p><strong>Before you continue</strong>, please take a moment to think about it: how you would implement it if you were asked to during an interview or a job. What data structures would you use? How would it work?</p><p>For this task, please:</p><ul>
<li>Read <a href="http://www.phpinternalsbook.com/hashtables/basic_structure.html">PHP Internals Book: HashTable</a></li>
<li>Use the same hash function</li>
<li>Use these data structures:</li>
</ul><pre><code>/**
 * struct shash_node_s - Node of a sorted hash table
 *
 * @key: The key, string
 * The key is unique in the HashTable
 * @value: The value corresponding to a key
 * @next: A pointer to the next node of the List
 * @sprev: A pointer to the previous element of the sorted linked list
 * @snext: A pointer to the next element of the sorted linked list
 */
typedef struct shash_node_s
{
     char *key;
     char *value;
     struct shash_node_s *next;
     struct shash_node_s *sprev;
     struct shash_node_s *snext;
} shash_node_t;

/**
 * struct shash_table_s - Sorted hash table data structure
 *
 * @size: The size of the array
 * @array: An array of size @size
 * Each cell of this array is a pointer to the first node of a linked list,
 * because we want our HashTable to use a Chaining collision handling
 * @shead: A pointer to the first element of the sorted linked list
 * @stail: A pointer to the last element of the sorted linked list
 */
typedef struct shash_table_s
{
     unsigned long int size;
     shash_node_t **array;
     shash_node_t *shead;
     shash_node_t *stail;
} shash_table_t;
</code></pre><p>Rewrite the previous functions using those data structures:</p><ul>
<li><code>shash_table_t *shash_table_create(unsigned long int size);</code></li>
<li><code>int shash_table_set(shash_table_t *ht, const char *key, const char *value);</code>
<ul>
<li>The key/value pair should be inserted in the sorted list at the right place</li>
<li>Note that here we do not want to do exactly like <code>PHP</code>: we want to create a sorted linked list, by key (sorted on ASCII value), that we can print by traversing it. See example.</li>
</ul></li>
<li><code>char *shash_table_get(const shash_table_t *ht, const char *key);</code></li>
<li><code>void shash_table_print(const shash_table_t *ht);</code>
<ul>
<li>Should print the hash table using the sorted linked list</li>
</ul></li>
<li><code>void shash_table_print_rev(const shash_table_t *ht);</code>
<ul>
<li>Should print the hash tables key/value pairs in reverse order using the sorted linked list</li>
</ul></li>
<li><code>void shash_table_delete(shash_table_t *ht);</code></li>
<li>You are allowed to have more than 5 functions in your file</li>
</ul><pre><code>julien@ubuntu:~/0x19. Hash tables$ cat 100-main.c 
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "hash_tables.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    shash_table_t *ht;

    ht = shash_table_create(1024);
    shash_table_set(ht, "y", "0");
    shash_table_print(ht);
    shash_table_set(ht, "j", "1");
    shash_table_print(ht);
    shash_table_set(ht, "c", "2");
    shash_table_print(ht);
    shash_table_set(ht, "b", "3");
    shash_table_print(ht);
    shash_table_set(ht, "z", "4");
    shash_table_print(ht);
    shash_table_set(ht, "n", "5");
    shash_table_print(ht);
    shash_table_set(ht, "a", "6");
    shash_table_print(ht);
    shash_table_set(ht, "m", "7");
    shash_table_print(ht);
    shash_table_print_rev(ht);
        shash_table_delete(ht);
    return (EXIT_SUCCESS);
}
julien@ubuntu:~/0x19. Hash tables$ gcc -Wall -pedantic -Werror -Wextra 100-main.c 100-sorted_hash_table.c 1-djb2.c 2-key_index.c -o sht 
julien@ubuntu:~/0x19. Hash tables$ ./sht 
{'y': '0'}
{'j': '1', 'y': '0'}
{'c': '2', 'j': '1', 'y': '0'}
{'b': '3', 'c': '2', 'j': '1', 'y': '0'}
{'b': '3', 'c': '2', 'j': '1', 'y': '0', 'z': '4'}
{'b': '3', 'c': '2', 'j': '1', 'n': '5', 'y': '0', 'z': '4'}
{'a': '6', 'b': '3', 'c': '2', 'j': '1', 'n': '5', 'y': '0', 'z': '4'}
{'a': '6', 'b': '3', 'c': '2', 'j': '1', 'm': '7', 'n': '5', 'y': '0', 'z': '4'}
{'z': '4', 'y': '0', 'n': '5', 'm': '7', 'j': '1', 'c': '2', 'b': '3', 'a': '6'}
julien@ubuntu:~/0x19. Hash tables$ 
</code></pre><p><br>
<img src="http://kraken-php.com/build/img/index/logo-php-adbac78231.png" width="50%"/></br></p>

