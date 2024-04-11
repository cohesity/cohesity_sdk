# Third-party import.
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.helios_mcm.v1.mcm_v1_client import McmV1Client
from cohesity_sdk.helios_mcm.v2.mcm_v2_client import McmV2Client

from config import (
    helios_ip,
    helios_api_key,
    cluster_vip,
    cluster_username,
    cluster_password,
    cluster_domain,
)


def helios_connector():
    """
    Function to create V1 Helios client.
    returns: client
    """
    client = McmV1Client(cluster_vip=helios_ip, api_key=helios_api_key)
    return client


def helios_v2_connector():
    """
    Function to create V2 Helios client.
    returns: client
    """
    client = McmV2Client(
        cluster_vip=helios_ip,
        api_key=helios_api_key,
    )
    return client


def helios_v2_connector_with_cluster_id():
    """
    Function to create V2 Helios client with cluster Id in headers.
    returns: client
    """
    # Fetch the cluster Id.
    cluster_client = ClusterClient(
        cluster_vip=cluster_vip,
        username=cluster_username,
        password=cluster_password,
        domain=cluster_domain,
    )
    cluster_id = cluster_client.platform.get_cluster().id
    client = McmV2Client(
        cluster_vip=helios_ip,
        api_key=helios_api_key,
        access_cluster_id=cluster_id,
    )
    return client
