# get all contributors from a repo: github.com/vesoft-inc/nebula-graph

# 1. get all contributors from a repo   

# 获取nebulagraph repo的所有contributors，和贡献数
curl -s -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/vesoft-inc/nebula-graph/contributors | jq '.[] | {login: .login, contributions: .contributions}' | jq 'sort_by(.contributions) | reverse'