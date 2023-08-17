#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints bytes information
*
* @p: Python Object
* Return: no return
*/
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AS_STRING(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        unsigned char byte = string[i];
        printf(" %02x", byte);
    }

    printf("\n");
}

/**
* print_python_list - Prints list information
*
* @p: Python Object
* Return: no return
*/

void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;

    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}

int main(void)
{
    Py_Initialize();
    PyObject *bytes_obj = PyBytes_FromString("Hello, Python!");
    PyObject *list_obj = PyList_New(3);
    PyList_SetItem(list_obj, 0, PyLong_FromLong(42));
    PyList_SetItem(list_obj, 1, bytes_obj);
    PyList_SetItem(list_obj, 2, PyUnicode_FromString("text"));

    print_python_bytes(bytes_obj);
    print_python_list(list_obj);

    Py_Finalize();

    return 0;
}
