"""
Python Sample to fetch all the views.
"""

from cohesity_sdk.helios.mcm_v2_client import McmV2Client

cluster_id = 00000000
# Create a client.
helios_client = McmV2Client(
    cluster_vip="x.x.x.x.x.x",
    api_key="xxxxx"
)


# Fetch list of views available in the cluster.
resp = helios_client.view_api.get_views(access_cluster_id=cluster_id)
print(resp)