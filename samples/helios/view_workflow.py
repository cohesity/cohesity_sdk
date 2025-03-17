"""
Python Sample to fetch all the views.
"""

from cohesity_sdk.helios.mcm_v2_client import McmV2Client

# Create a client.
helios_client = McmV2Client(
    api_key="xxxxx",
    access_cluster_id="x.x.x.x",
    cluster_vip="helios.cohesity.com"
)


# Fetch list of views available in the cluster.
resp = helios_client.view_api.get_views()
print(resp)