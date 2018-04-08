# HITCON-Training lab11

## binary analysis

> Makefile
```
bamboobox:bamboobox.c
	gcc bamboobox.c -o bamboobox
```

I used this structure to analysis easier.

```c
struct Note {
  int (__cdecl *print)(int);
  char *buf;
};
```

![](main.PNG)

## solve

```python

```