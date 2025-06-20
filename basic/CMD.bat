@echo off
for /f "skip=1 tokens=1-2 delims= " %%A in ('kubectl get pods --all-namespaces') do @echo %%B