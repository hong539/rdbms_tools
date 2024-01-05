from celery import Celery
import subprocess

# 创建 Celery 实例
app = Celery('tasks', broker='redis://localhost:6379/0')  # 使用 Redis 作为消息代理

# 定义执行 Bash 脚本的任务
@app.task
def run_bash_script(script_path):
    try:
        # 执行 Bash 脚本
        result = subprocess.run(['bash', script_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error executing script: {e}"