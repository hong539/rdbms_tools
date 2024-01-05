from tasks import run_bash_script

# 指定要执行的 Bash 脚本路径
script_path = '/path/to/your/script.sh'

# 调用 Celery 任务执行 Bash 脚本
result = run_bash_script.delay(script_path)
print(result.get())  # 获取任务执行结果