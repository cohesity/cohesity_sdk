from cohesity_sdk.cluster.cluster_client import ClusterClient

from cohesity_sdk.cluster.model.create_view_request import CreateViewRequest
from cohesity_sdk.cluster.model.view_protocol import ViewProtocol
from cohesity_sdk.cluster.model.qo_s import QoS


def get_view_box_id(name="DefaultStorageDomain"):
    try:
        storage_domains = client.storage_domains.get_storage_domains().storage_domains
        for domain in storage_domains:
            print(domain.name)
            if domain.name == name:
                return domain.id
        raise Exception(
            "Storage domain with name %s is not available" % name)
    except Exception as err:
        print("Error while fetching storage domains")
        exit()


def get_policy_by_name(name):
    try:
        policies = client.protection_policies
        existing_policies = policies.get_protection_policies().policies
        for policy in existing_policies:
            if policy.name == name:
                return policy.id
        return -1
    except Exception as err:
        print(
            "Error while fetching protection policies, err msg '%s'" % err)
        exit()


def get_views(name):
    try:
        views = client.views.get_views().views
        for view in views:
            if view.name == name:
                return view.view_id
    except Exception as err:
        print(
            "Error while fetching views, err msg '%s'" % err)
        exit()


def create_view(name):
    try:
        view_protocol = ViewProtocol(type="NFS", mode="ReadWrite")
        body = CreateViewRequest(
            storage_domain_id=get_view_box_id("Default-Storage-Domain"),
            name=name,
            case_insensitive_names_enabled=False,
            category='FileServices',
            protocol_access=[view_protocol]
            )
        views = client.views.create_view(body)
    except Exception as err:
        print(
            "Error while creating view, err msg '%s'" % err)
        exit()







if __name__ == "__main__":
    client = ClusterClient(
        "10.2.145.49", api_key="0755ab14-39a1-4062-4858-79db66d632a6"
    )
    create_view(name="new_v2___SDK")
    
