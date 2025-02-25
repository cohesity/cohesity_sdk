from cohesity_sdk.helios.configuration import Configuration
from cohesity_sdk.helios.api_client import ApiClient
from cohesity_sdk.helios.exceptions import ApiException
from cohesity_sdk.helios.model.create_access_token_request_params import (
    CreateAccessTokenRequestParams,
)


from cohesity_sdk.helios.api.access_token import AccessTokenApi
from cohesity_sdk.helios.api.active_directory import ActiveDirectoryApi
from cohesity_sdk.helios.api.agent import AgentApi
from cohesity_sdk.helios.api.alert import AlertApi
from cohesity_sdk.helios.api.antivirus_service import AntivirusServiceApi
from cohesity_sdk.helios.api.audit_log import AuditLogApi
from cohesity_sdk.helios.api.aws_registration import AwsRegistrationApi
from cohesity_sdk.helios.api.certificate import CertificateApi
from cohesity_sdk.helios.api.cloud_retrieve_task import CloudRetrieveTaskApi
from cohesity_sdk.helios.api.cluster_management import ClusterManagementApi
from cohesity_sdk.helios.api.connectors import ConnectorsApi
from cohesity_sdk.helios.api.copy_stats import CopyStatsApi
from cohesity_sdk.helios.api.customize_ui import CustomizeUIApi
from cohesity_sdk.helios.api.d_maa_s_tenant_certificate import DMaaSTenantCertificateApi
from cohesity_sdk.helios.api.data_tiering import DataTieringApi
from cohesity_sdk.helios.api.external_connection import ExternalConnectionApi
from cohesity_sdk.helios.api.external_target import ExternalTargetApi
from cohesity_sdk.helios.api.failover import FailoverApi
from cohesity_sdk.helios.api.firewall import FirewallApi
from cohesity_sdk.helios.api.fleet_instance import FleetInstanceApi
from cohesity_sdk.helios.api.fort_knox import FortKnoxApi
from cohesity_sdk.helios.api.helios_accounts import HeliosAccountsApi
from cohesity_sdk.helios.api.helios_claim import HeliosClaimApi
from cohesity_sdk.helios.api.helios_data_protect_stats import HeliosDataProtectStatsApi
from cohesity_sdk.helios.api.helios_login_configuration import (
    HeliosLoginConfigurationApi,
)
from cohesity_sdk.helios.api.helios_notifications import HeliosNotificationsApi
from cohesity_sdk.helios.api.helios_on_prem import HeliosOnPremApi
from cohesity_sdk.helios.api.helios_signup import HeliosSignupApi
from cohesity_sdk.helios.api.ips import IPsApi
from cohesity_sdk.helios.api.identity_provider import IdentityProviderApi
from cohesity_sdk.helios.api.indexing_cloud_config import IndexingCloudConfigApi
from cohesity_sdk.helios.api.internal import InternalApi
from cohesity_sdk.helios.api.kerberos_provider import KerberosProviderApi
from cohesity_sdk.helios.api.key_management_system import KeyManagementSystemApi
from cohesity_sdk.helios.api.keystone import KeystoneApi
from cohesity_sdk.helios.api.ldap import LDAPApi
from cohesity_sdk.helios.api.mfa import MFAApi
from cohesity_sdk.helios.api.marketplace_app import MarketplaceAppApi
from cohesity_sdk.helios.api.network_information_service import (
    NetworkInformationServiceApi,
)
from cohesity_sdk.helios.api.node_group import NodeGroupApi
from cohesity_sdk.helios.api.object import ObjectApi
from cohesity_sdk.helios.api.patch_management import PatchManagementApi
from cohesity_sdk.helios.api.platform import PlatformApi
from cohesity_sdk.helios.api.policy import PolicyApi
from cohesity_sdk.helios.api.privilege import PrivilegeApi
from cohesity_sdk.helios.api.protected_object import ProtectedObjectApi
from cohesity_sdk.helios.api.protection_group import ProtectionGroupApi
from cohesity_sdk.helios.api.recovery import RecoveryApi
from cohesity_sdk.helios.api.registration import RegistrationApi
from cohesity_sdk.helios.api.remote_clusters import RemoteClustersApi
from cohesity_sdk.helios.api.remote_storage import RemoteStorageApi
from cohesity_sdk.helios.api.role import RoleApi
from cohesity_sdk.helios.api.routes import RoutesApi
from cohesity_sdk.helios.api.rpaas import RpaasApi
from cohesity_sdk.helios.api.search import SearchApi
from cohesity_sdk.helios.api.security import SecurityApi
from cohesity_sdk.helios.api.source import SourceApi
from cohesity_sdk.helios.api.stats import StatsApi
from cohesity_sdk.helios.api.storage_domain import StorageDomainApi
from cohesity_sdk.helios.api.syslog import SyslogApi
from cohesity_sdk.helios.api.tag import TagApi
from cohesity_sdk.helios.api.tagging_service import TaggingServiceApi
from cohesity_sdk.helios.api.tasks import TasksApi
from cohesity_sdk.helios.api.tenant import TenantApi
from cohesity_sdk.helios.api.test_data_management import TestDataManagementApi
from cohesity_sdk.helios.api.uda_connector_config import UdaConnectorConfigApi
from cohesity_sdk.helios.api.user import UserApi
from cohesity_sdk.helios.api.view import ViewApi
from cohesity_sdk.helios.api.network_reset import NetworkResetApi
from cohesity_sdk.helios.api.runbooks import RunbooksApi

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


class HeliosClient:
    def __init__(
        self,
        api_key=None,
        access_cluster_id=None,
        cluster_vip=None,
        region_id=None,
        auth_timeout=30,
    ):
        # self.domain = domain
        # self.username = username
        # self.password = password
        self.api_key = api_key
        self.access_cluster_id = access_cluster_id
        self.region_id = region_id

        self.auth_timeout = auth_timeout

        self.configuration = Configuration()

        # TODO: remove this once the backend has ssl certificate setup
        self.configuration.verify_ssl = False

        if cluster_vip != None:
            host = re.sub("localhost", cluster_vip, self.configuration._base_path)
            host = re.sub("http:", "https:", host)
            self.configuration.host = host
        else:
            self.configuration.host = "https://helios.cohesity.com/v2"

        # This fixes the response type conflict between the backend and Swagger spec file
        self.configuration.discard_unknown_keys = True

        if api_key == None:
            raise Exception(
                "Fail to initialize a client. Please provide authentication info."
            )

        self.__authenticate()

    """
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
                if self.access_cluster_id != None and self.region_id != None:
                    return api_instance.create_access_token(
                        body,
                        access_cluster_id=self.access_cluster_id,
                        region_id=self.region_id,
                        _request_timeout=self.auth_timeout
                    )
                elif self.access_cluster_id != None:
                    return api_instance.create_access_token(
                        body,
                        access_cluster_id=self.access_cluster_id,
                        _request_timeout=self.auth_timeout
                    )
                elif self.region_id != None:
                    return api_instance.create_access_token(
                        body,
                        region_id=self.region_id,
                        _request_timeout=self.auth_timeout
                    )
                else:
                    return api_instance.create_access_token(
                        body,
                        _request_timeout=self.auth_timeout
                    )

            except MaxRetryError as e:
                raise ApiException(status=404, reason=str(e)) from None
    """

    def __authenticate(self):
        """
        if self.username and self.password and self.domain:
            token = self.__get_token()
            self.configuration.api_key['TokenHeader'] = token.token_type + ' ' + token.access_token
        """
        if self.api_key:
            self.configuration.api_key["APIKeyHeader"] = self.api_key

        if self.access_cluster_id:
            self.configuration.api_key["ClusterId"] = self.access_cluster_id

    @lazy_property
    def access_token(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AccessTokenApi(api_client)

    @lazy_property
    def active_directory(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ActiveDirectoryApi(api_client)

    @lazy_property
    def agent(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AgentApi(api_client)

    @lazy_property
    def alert(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AlertApi(api_client)

    @lazy_property
    def antivirus_service(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AntivirusServiceApi(api_client)

    @lazy_property
    def audit_log(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AuditLogApi(api_client)

    @lazy_property
    def aws_registration(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AwsRegistrationApi(api_client)

    @lazy_property
    def certificate(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CertificateApi(api_client)

    @lazy_property
    def cloud_retrieve_task(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CloudRetrieveTaskApi(api_client)

    @lazy_property
    def cluster_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ClusterManagementApi(api_client)

    @lazy_property
    def connectors(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ConnectorsApi(api_client)

    @lazy_property
    def copy_stats(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CopyStatsApi(api_client)

    @lazy_property
    def customize_ui(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CustomizeUIApi(api_client)

    @lazy_property
    def d_maa_s_tenant_certificate(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return DMaaSTenantCertificateApi(api_client)

    @lazy_property
    def data_tiering(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return DataTieringApi(api_client)

    @lazy_property
    def external_connection(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ExternalConnectionApi(api_client)

    @lazy_property
    def external_target(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ExternalTargetApi(api_client)

    @lazy_property
    def failover(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FailoverApi(api_client)

    @lazy_property
    def firewall(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FirewallApi(api_client)

    @lazy_property
    def fleet_instance(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FleetInstanceApi(api_client)

    @lazy_property
    def fort_knox(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FortKnoxApi(api_client)

    @lazy_property
    def helios_accounts(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosAccountsApi(api_client)

    @lazy_property
    def helios_claim(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosClaimApi(api_client)

    @lazy_property
    def helios_data_protect_stats(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosDataProtectStatsApi(api_client)

    @lazy_property
    def helios_login_configuration(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosLoginConfigurationApi(api_client)

    @lazy_property
    def helios_notifications(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosNotificationsApi(api_client)

    @lazy_property
    def helios_on_prem(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosOnPremApi(api_client)

    @lazy_property
    def helios_signup(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosSignupApi(api_client)

    @lazy_property
    def ips(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IPsApi(api_client)

    @lazy_property
    def identity_provider(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IdentityProviderApi(api_client)

    @lazy_property
    def indexing_cloud_config(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IndexingCloudConfigApi(api_client)

    @lazy_property
    def internal(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return InternalApi(api_client)

    @lazy_property
    def kerberos_provider(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KerberosProviderApi(api_client)

    @lazy_property
    def key_management_system(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeyManagementSystemApi(api_client)

    @lazy_property
    def keystone(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeystoneApi(api_client)

    @lazy_property
    def ldap(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return LDAPApi(api_client)

    @lazy_property
    def mfa(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MFAApi(api_client)

    @lazy_property
    def marketplace_app(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MarketplaceAppApi(api_client)

    @lazy_property
    def network_information_service(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkInformationServiceApi(api_client)

    @lazy_property
    def node_group(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NodeGroupApi(api_client)

    @lazy_property
    def object(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ObjectApi(api_client)

    @lazy_property
    def patch_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PatchManagementApi(api_client)

    @lazy_property
    def platform(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PlatformApi(api_client)

    @lazy_property
    def policy(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PolicyApi(api_client)

    @lazy_property
    def privilege(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PrivilegeApi(api_client)

    @lazy_property
    def protected_object(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectedObjectApi(api_client)

    @lazy_property
    def protection_group(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionGroupApi(api_client)

    @lazy_property
    def recovery(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RecoveryApi(api_client)

    @lazy_property
    def registration(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RegistrationApi(api_client)

    @lazy_property
    def remote_clusters(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteClustersApi(api_client)

    @lazy_property
    def remote_storage(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteStorageApi(api_client)

    @lazy_property
    def role(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoleApi(api_client)

    @lazy_property
    def routes(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoutesApi(api_client)

    @lazy_property
    def rpaas(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RpaasApi(api_client)

    @lazy_property
    def search(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SearchApi(api_client)

    @lazy_property
    def security(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SecurityApi(api_client)

    @lazy_property
    def source(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SourceApi(api_client)

    @lazy_property
    def stats(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StatsApi(api_client)

    @lazy_property
    def storage_domain(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StorageDomainApi(api_client)

    @lazy_property
    def syslog(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SyslogApi(api_client)

    @lazy_property
    def tag(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TagApi(api_client)

    @lazy_property
    def tagging_service(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TaggingServiceApi(api_client)

    @lazy_property
    def tasks(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TasksApi(api_client)

    @lazy_property
    def tenant(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TenantApi(api_client)

    @lazy_property
    def test_data_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TestDataManagementApi(api_client)

    @lazy_property
    def uda_connector_config(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UdaConnectorConfigApi(api_client)

    @lazy_property
    def user(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UserApi(api_client)

    @lazy_property
    def view(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ViewApi(api_client)

    @lazy_property
    def network_reset(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkResetApi(api_client)

    @lazy_property
    def runbooks(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RunbooksApi(api_client)
