import time
import threading


def do_task(processor_id, tasks):
    print(f"Processor {processor_id} mulai dengan {len(tasks)} task")

    for task in tasks:
        print(f"Processor {processor_id} mengerjakan task {task}")
        time.sleep(0.5)

    print(f"Processor {processor_id} selesai")


tasks = list(range(1, 11))

# Static Uneven Distribution
processor_tasks = {
    1: tasks[0:5],
    2: tasks[5:8],
    3: tasks[8:10]
}

threads = []

start_time = time.time()

for processor_id, task_list in processor_tasks.items():
    t = threading.Thread(
        target=do_task,
        args=(processor_id, task_list)
    )

    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

task_counts = [len(x) for x in processor_tasks.values()]
ideal = sum(task_counts) / len(task_counts)

print("\n=== ANALISIS DISTRIBUSI ===")
print("Task per processor :", task_counts)
print("Ideal Distribution :", ideal)

for i, count in enumerate(task_counts):
    diff = abs(count - ideal)

    print(
        f"Processor {i+1} -> "
        f"{count} task "
        f"(selisih {diff:.2f})"
    )

if max(task_counts) - min(task_counts) <= 1:
    print("\nDistribusi mencapai kondisi ideal")
else:
    print("\nDistribusi belum mencapai kondisi ideal")

print(
    f"\nTotal waktu eksekusi : "
    f"{end_time-start_time:.2f} detik"
)