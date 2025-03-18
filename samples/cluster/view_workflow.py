"""
Python Sample to fetch all the views and create a protection job.
"""


from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.models.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)
from cohesity_sdk.cluster.models.view_protection_group_params import (
    ViewProtectionGroupParams,
)
from cohesity_sdk.cluster.models.view_protection_group_object_params import (
    ViewProtectionGroupObjectParams,
)

# Create a client.
v2_client = ClusterClient(
    "x.x.x.x", username="admin", password="admin", domain="LOCAL"
)

# Get Policy ID
policies = v2_client.policy_api.get_protection_policies().policies
for policy in policies:
    if policy.name == "Bronze":
        policy_id = policy.id

# Fetch list of views available in the cluster.
objects = list()
for view in v2_client.view_api.get_views().views:
    objects.append(ViewProtectionGroupObjectParams(id=view.view_id))

view_params = ViewProtectionGroupParams(objects=objects)

body = CreateOrUpdateProtectionGroupRequest(
    storage_domain_id=2,
    policy_id=policy_id,
    name="ViewJob",
    environment="kView",
    view_params=view_params,
)
resp = v2_client.protection_group_api.create_protection_group(body)

job = v2_client.protection_group_api.get_protection_group_by_id(resp.id)
print(job)