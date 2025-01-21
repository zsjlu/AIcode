# kubectl 获取所有pods，按照restart count排序

# 1.获取所有pods命令
kubectl get pods --all-namespaces -o json | jq '.items[] | {name: .metadata.name, namespace: .metadata.namespace, restartCount: .status.containerStatuses[].restartCount}' | sort -k 3 -n   

