
from kubernetes import client, config

# Load the k8s config 

config.load_kube_config()

# create api 
v1 = client.CoreV1Api()

# set namespace

namespace = "test-demo"
pod_name = "script-test"
container_name = "script-test"

try:
    pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, container=container_name, tail_lines=30)

    for container_status in pod.status.container_statuses:
        container_name = container_status.name 
        liveness_status = container_status.state
        readiness_status = container_status.ready 


        print(f"Container: {container_name}")
        if liveness_status.running:
            print("✅ Liveness Probe: Running")
        elif liveness_status.terminated:
            print(f"❌ Liveness Probe: Failed (Container Terminated)")
        elif liveness_status.waiting:
            print(f"⏳ Liveness Probe: Wating for startup")

        print(f"🔎 Readiness Probe: {'Ready ✅' if readiness_status else 'Not Ready ❌'}")
        print("-" * 40)
    
    print(f"logs for the container: {container_name} in pod {pod_name}")
    print(logs)


except client.exceptions.ApiException as e:
    print(f"Error fetching pod data: {e.reason}")


# with open("logs.txt", "w") as file:
#     file.write(logs)
#     print(f"Log file can be found in the current dir")