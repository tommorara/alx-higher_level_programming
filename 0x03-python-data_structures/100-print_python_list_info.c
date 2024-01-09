#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info-C function that prints
 * some basic info about Python lists
 * @p: python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	size_t size, allocated, q;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (q = 0; q < size; ++q)
	{
		obj = PyList_GetItem(p, q);
		printf("Element %ld: %s\n", q, Py_TYPE(obj)->tp_name);
	}
}
