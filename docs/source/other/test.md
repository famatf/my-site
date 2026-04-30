# 备忘录

```bat
cd /d G:\docs_site
rmdir /s /q docs\build
sphinx-build -b html -E -a docs/source docs/build/html
start docs\build\html\index.html
```

```bat
sphinx-autobuild -a -E docs/source docs/build/html
```

111
待补充