from typing import TypeVar, Any
from generics import Stack
from protocol import DataManager, LocalDiscSaver, Report

T = TypeVar("T")


def add(a: int, b: int):
    return a + b


print(f'"a" + "b" = {add("a", "b")}')
print(f"1 + 2 = {add(1, 2)}")
print(f'"a" + 2 = {add("a", 2)}')


################################################


def add_to_stack_typed(stack: Stack[T], val: T):
    stack.push(val)


def add_to_stack(stack: Stack, val: Any):
    stack.push(val)


x = Stack[int]()
x.push(1)
x.push(2)
x.push(3)
z = x.pop()


add_to_stack_typed(x, 5)


# sometimes cryptic error messages
add_to_stack_typed(x, "abc")

add_to_stack(x, "def")

################################################

x = Report(
    customer_id=1,
    customer_name="very important",
    information={"KPI1": 1, "KPI2": "qualitative information"},
)

manager = DataManager(LocalDiscSaver())
manager.transform(x)
