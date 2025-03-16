from cohesity_sdk.cluster.configuration import Configuration
from cohesity_sdk.cluster.api_client import ApiClient
from cohesity_sdk.cluster.exceptions import ApiException
from cohesity_sdk.cluster.models.create_access_token_request_params import CreateAccessTokenRequestParams


from cohesity_sdk.cluster.api.access_token_api import AccessTokenApi
from cohesity_sdk.cluster.api.active_directory_api import ActiveDirectoryApi
from cohesity_sdk.cluster.api.agent_api import AgentApi
from cohesity_sdk.cluster.api.alert_api import AlertApi
from cohesity_sdk.cluster.api.antivirus_service_api import AntivirusServiceApi
from cohesity_sdk.cluster.api.audit_log_api import AuditLogApi
from cohesity_sdk.cluster.api.baseos_patch_management_api import BaseosPatchManagementApi
from cohesity_sdk.cluster.api.cloud_retrieve_task_api import CloudRetrieveTaskApi
from cohesity_sdk.cluster.api.data_tiering_api import DataTieringApi
from cohesity_sdk.cluster.api.external_target_api import ExternalTargetApi
from cohesity_sdk.cluster.api.failover_api import FailoverApi
from cohesity_sdk.cluster.api.firewall_api import FirewallApi
from cohesity_sdk.cluster.api.helios_on_prem_api import HeliosOnPremApi
from cohesity_sdk.cluster.api.ips_api import IPsApi
from cohesity_sdk.cluster.api.identity_provider_api import IdentityProviderApi
from cohesity_sdk.cluster.api.kerberos_provider_api import KerberosProviderApi
from cohesity_sdk.cluster.api.key_management_system_api import KeyManagementSystemApi
from cohesity_sdk.cluster.api.keystone_api import KeystoneApi
from cohesity_sdk.cluster.api.ldap_api import LDAPApi
from cohesity_sdk.cluster.api.mfa_api import MFAApi
from cohesity_sdk.cluster.api.node_group_api import NodeGroupApi
from cohesity_sdk.cluster.api.object_api import ObjectApi
from cohesity_sdk.cluster.api.patch_management_api import PatchManagementApi
from cohesity_sdk.cluster.api.platform_api import PlatformApi
from cohesity_sdk.cluster.api.policy_api import PolicyApi
from cohesity_sdk.cluster.api.privilege_api import PrivilegeApi
from cohesity_sdk.cluster.api.protected_object_api import ProtectedObjectApi
from cohesity_sdk.cluster.api.protection_group_api import ProtectionGroupApi
from cohesity_sdk.cluster.api.recovery_api import RecoveryApi
from cohesity_sdk.cluster.api.registration_api import RegistrationApi
from cohesity_sdk.cluster.api.remote_clusters_api import RemoteClustersApi
from cohesity_sdk.cluster.api.remote_storage_api import RemoteStorageApi
from cohesity_sdk.cluster.api.role_api import RoleApi
from cohesity_sdk.cluster.api.routes_api import RoutesApi
from cohesity_sdk.cluster.api.search_api import SearchApi
from cohesity_sdk.cluster.api.security_api import SecurityApi
from cohesity_sdk.cluster.api.source_api import SourceApi
from cohesity_sdk.cluster.api.stats_api import StatsApi
from cohesity_sdk.cluster.api.storage_domain_api import StorageDomainApi
from cohesity_sdk.cluster.api.support_api import SupportApi
from cohesity_sdk.cluster.api.syslog_api import SyslogApi
from cohesity_sdk.cluster.api.tag_api import TagApi
from cohesity_sdk.cluster.api.templates_api import TemplatesApi
from cohesity_sdk.cluster.api.tenant_api import TenantApi
from cohesity_sdk.cluster.api.user_api import UserApi
from cohesity_sdk.cluster.api.view_api import ViewApi

import re
from urllib3.exceptions import MaxRetryError

class lazy_property(object):

    """A decorator class for lazy instantiation."""

    def __init__(self, fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj, self.func_name, value)
        return value


# class Client:
class ClusterClient:
    def __init__(self,
        cluster_vip = None,
        username = None,
        password = None,
        domain = None,
        api_key = None,
        auth_timeout = 30
    ):

        self.domain = domain
        self.username = username
        self.password = password
        self.api_key = api_key
        self.auth_timeout = auth_timeout

        self.configuration = Configuration()
        if cluster_vip != None:
            self.configuration.host = f"https://{cluster_vip}/v2"
        else:
            raise Exception('Missing cluster_vip info to initialize a client.')

        # TODO: remove this later, python in MacOS Catalina has a problem in verify SSL
        self.configuration.verify_ssl = False

        # This fixes the response type conflict between the backend and Swagger spec file
        self.configuration.discard_unknown_keys = True

        if username == None and password == None and api_key == None:
            raise Exception('Missing authentication info to initialize a client. \
                Please provide authentication info.')

        self.__authenticate()

    def __get_token(self):
        # TODO: change the hard-coded host

        with ApiClient(self.configuration) as api_client:
            api_instance = AccessTokenApi(api_client)
            body = CreateAccessTokenRequestParams(
                domain=self.domain,
                password=self.password,
                username=self.username
            )

            try:
                return api_instance.create_access_token(body, _request_timeout=self.auth_timeout)
            except MaxRetryError as e:
                raise ApiException(status=404, reason=str(e)) from None

    def __authenticate(self):
        if self.username and self.password and self.domain:
            token = self.__get_token()
            self.configuration.api_key['Bearer'] = token.token_type + ' ' + token.access_token
        elif self.api_key:
            self.configuration.api_key['APIKeyHeader'] = self.api_key



    @lazy_property
    def access_token_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AccessTokenApi(api_client)

    @lazy_property
    def active_directory_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ActiveDirectoryApi(api_client)

    @lazy_property
    def agent_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AgentApi(api_client)

    @lazy_property
    def alert_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AlertApi(api_client)

    @lazy_property
    def antivirus_service_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AntivirusServiceApi(api_client)

    @lazy_property
    def audit_log_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AuditLogApi(api_client)

    @lazy_property
    def baseos_patch_management_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return BaseosPatchManagementApi(api_client)

    @lazy_property
    def cloud_retrieve_task_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CloudRetrieveTaskApi(api_client)

    @lazy_property
    def data_tiering_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return DataTieringApi(api_client)

    @lazy_property
    def external_target_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ExternalTargetApi(api_client)

    @lazy_property
    def failover_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FailoverApi(api_client)

    @lazy_property
    def firewall_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FirewallApi(api_client)

    @lazy_property
    def helios_on_prem_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosOnPremApi(api_client)

    @lazy_property
    def ips_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IPsApi(api_client)

    @lazy_property
    def identity_provider_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IdentityProviderApi(api_client)

    @lazy_property
    def kerberos_provider_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KerberosProviderApi(api_client)

    @lazy_property
    def key_management_system_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeyManagementSystemApi(api_client)

    @lazy_property
    def keystone_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeystoneApi(api_client)

    @lazy_property
    def ldap_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return LDAPApi(api_client)

    @lazy_property
    def mfa_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MFAApi(api_client)

    @lazy_property
    def node_group_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NodeGroupApi(api_client)

    @lazy_property
    def object_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ObjectApi(api_client)

    @lazy_property
    def patch_management_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PatchManagementApi(api_client)

    @lazy_property
    def platform_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PlatformApi(api_client)

    @lazy_property
    def policy_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PolicyApi(api_client)

    @lazy_property
    def privilege_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PrivilegeApi(api_client)

    @lazy_property
    def protected_object_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectedObjectApi(api_client)

    @lazy_property
    def protection_group_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionGroupApi(api_client)

    @lazy_property
    def recovery_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RecoveryApi(api_client)

    @lazy_property
    def registration_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RegistrationApi(api_client)

    @lazy_property
    def remote_clusters_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteClustersApi(api_client)

    @lazy_property
    def remote_storage_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteStorageApi(api_client)

    @lazy_property
    def role_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoleApi(api_client)

    @lazy_property
    def routes_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoutesApi(api_client)

    @lazy_property
    def search_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SearchApi(api_client)

    @lazy_property
    def security_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SecurityApi(api_client)

    @lazy_property
    def source_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SourceApi(api_client)

    @lazy_property
    def stats_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StatsApi(api_client)

    @lazy_property
    def storage_domain_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StorageDomainApi(api_client)

    @lazy_property
    def support_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SupportApi(api_client)

    @lazy_property
    def syslog_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SyslogApi(api_client)

    @lazy_property
    def tag_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TagApi(api_client)

    @lazy_property
    def templates_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TemplatesApi(api_client)

    @lazy_property
    def tenant_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TenantApi(api_client)

    @lazy_property
    def user_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UserApi(api_client)

    @lazy_property
    def view_api(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ViewApi(api_client)
