from prefect import flow, task
from typing import List
import httpx


@task
def hello_task():
    return "Hello"


@task
def world_task():
    return "World!"


@flow(name="Hello World")
def hello_world_flow() -> List[str]:
    hello = hello_task()
    print(hello)
    world = world_task()
    print(world)

    return [hello, world]


if __name__ == "__main__":
    # 手动调用
    # hello_world_flow()

    # hello_world_flow.serve(
    #     name="hello-world-flow",
    #     cron="*/10 * * * *"
    # )

    hello_world_flow.from_source(
        source="git@github.com:zhangqitao1/prefect.git",
        entrypoint="t1.py:hello_world_flow"
    ).deploy(
        name="hello-world-flow",
        work_pool_name="default-agent-pool",
        cron="*/10 * * * *"
    )
