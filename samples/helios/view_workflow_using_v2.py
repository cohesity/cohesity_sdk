import random

from cohesity_sdk.helios_mcm.v2.model.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)

from cohesity_sdk.helios_mcm.v2.model.create_view_request import CreateViewRequest
from cohesity_sdk.helios_mcm.v2.model.view_protection_group_params import (
    ViewProtectionGroupParams,
)
from cohesity_sdk.helios_mcm.v2.model.view_protection_group_object_params import (
    ViewProtectionGroupObjectParams,
)
from cohesity_sdk.helios_mcm.v2.model.view_protocol import ViewProtocol
from cohesity_sdk.helios_mcm.v2.model.qo_s import QoS

from helios_client import helios_v2_connector_with_cluster_id

# Initialise a client.
client = helios_v2_connector_with_cluster_id()
name = "ViewJob_" + str(random.randint(1, 100))
policy_id = client.policy.get_protection_policies().policies[0].id
domain_id = client.storage_domain.get_storage_domains().storage_domains[0].id


def create_view():
    """
    Function to create a view.
    """
    try:
        protocol_access = ViewProtocol(type="NFS", mode="ReadWrite")
        payload = CreateViewRequest(
            storage_domain_id=domain_id,
            name="View_" + str(random.randint(1, 100)),
            category="FileServices",
            protocol_access=[protocol_access],
            qos={},
        )
        response = client.view.create_view(payload)
        print(response)
        return response.view_id
    except Exception as err:
        print(err)


try:
    # Create a view, protect the view.
    views = client.view.get_views().views
    if not views:
        view_id = create_view()
    else:
        view_id = views[0].view_id
    view_id = create_view()
    payload = CreateOrUpdateProtectionGroupRequest(
        environment="kView",
        name=name,
        policy_id=policy_id,
        storage_domain_id=domain_id,
        view_params=ViewProtectionGroupParams(
            objects=[ViewProtectionGroupObjectParams(id=view_id)]
        ),
    )
    print("Creating protection job, name '%s'" % payload.name)
    resp = client.protection_group.create_protection_group(payload)
    job_id = resp.id
    # Delete the job.
    print("Deleting protection job and snapshots")
    resp = client.protection_group.delete_protection_group(
        job_id, delete_snapshots=True
    )
except Exception as err:
    print(err)
