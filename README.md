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
</div><p>In <a href="http://php.net/manual/en/intro-whatis.php">PHP</a>, hash tables are <strong>ordered</strong>. Wait... WAT? How is this even possible?</p><p><img src="https://media.giphy.com/media/IUp9WRHyCwUEg/giphy.gif"/><br/>
<br/></p><p><strong>Before you continue</strong>, please take a moment to think about it: how you would implement it if you were asked to during an interview or a job. What data structures would you use? How would it work?</p><p>For this task, please:</p><ul>
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
#   shash_table_set(ht, "y", "0");
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
</code></pre><p><br/>
<img src="http://kraken-php.com/build/img/index/logo-php-adbac78231.png" width="50%"/></p>

