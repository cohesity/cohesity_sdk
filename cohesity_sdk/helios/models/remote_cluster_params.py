# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.replication_params import ReplicationParams
from typing import Set
from typing_extensions import Self

class RemoteClusterParams(BaseModel):
    """
    Specifies the parameters to update a Remote Cluster config.
    """ # noqa: E501
    auto_register_target: Optional[StrictBool] = Field(default=False, description="Specifies if the Tx clusters should be automatically registered at the Rx site.", alias="autoRegisterTarget")
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the Remote Cluster id.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the Remote Cluster incarnation id.", alias="clusterIncarnationId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Specifies the Remote Cluster name.", alias="clusterName")
    description: Optional[StrictStr] = Field(default=None, description="Specifies any additional information if needed.")
    effective_aes_encryption_mode: Optional[StrictStr] = Field(default=None, description="Specifies the effective AES Encryption mode negotiated between local and the remote cluster.", alias="effectiveAesEncryptionMode")
    is_auto_registered: Optional[StrictBool] = Field(default=None, description="Specifies if the Remote Cluster was registered automatically or manually.", alias="isAutoRegistered")
    local_addresses: Optional[List[StrictStr]] = Field(default=None, description="Specifies the IP addresses of the interfaces in the local Cluster which will be used for communicating with the remote Cluster.", alias="localAddresses")
    multi_tenancy_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if the Remote Cluster has Multi-Tenancy enabled.", alias="multiTenancyEnabled")
    network_interface: Optional[StrictStr] = Field(default=None, description="Specifies the name of the network interfaces to use for communicating with the Remote Cluster.", alias="networkInterface")
    purpose: Optional[List[StrictStr]] = Field(default=None, description="Specifies the purpose for which the remote cluster is being registered.")
    replication_params: Optional[ReplicationParams] = Field(default=None, alias="replicationParams")
    supported_aes_encryption_mode: Optional[StrictStr] = Field(default=None, description="Specifies the AES Encryption mode of the remote cluster.", alias="supportedAesEncryptionMode")
    tenant_storage_domain_sharing_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if Tenant Storage Domain sharing is enabled on the Remote Cluster.", alias="tenantStorageDomainSharingEnabled")
    tls_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if TLS is enabled on the Remote Cluster.", alias="tlsEnabled")
    __properties: ClassVar[List[str]] = ["autoRegisterTarget", "clusterId", "clusterIncarnationId", "clusterName", "description", "effectiveAesEncryptionMode", "isAutoRegistered", "localAddresses", "multiTenancyEnabled", "networkInterface", "purpose", "replicationParams", "supportedAesEncryptionMode", "tenantStorageDomainSharingEnabled", "tlsEnabled"]

    @field_validator('effective_aes_encryption_mode')
    def effective_aes_encryption_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CBC', 'GCM']):
            raise ValueError("must be one of enum values ('CBC', 'GCM')")
        return value

    @field_validator('purpose')
    def purpose_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Replication', 'RemoteAccess']):
                raise ValueError("each list item must be one of ('Replication', 'RemoteAccess')")
        return value

    @field_validator('supported_aes_encryption_mode')
    def supported_aes_encryption_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CBC', 'GCM']):
            raise ValueError("must be one of enum values ('CBC', 'GCM')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RemoteClusterParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "cluster_id",
            "cluster_incarnation_id",
            "cluster_name",
            "is_auto_registered",
            "local_addresses",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of replication_params
        if self.replication_params:
            _dict['replicationParams'] = self.replication_params.to_dict()
        # set to None if auto_register_target (nullable) is None
        # and model_fields_set contains the field
        if self.auto_register_target is None and "auto_register_target" in self.model_fields_set:
            _dict['autoRegisterTarget'] = None

        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationId'] = None

        # set to None if cluster_name (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_name is None and "cluster_name" in self.model_fields_set:
            _dict['clusterName'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if effective_aes_encryption_mode (nullable) is None
        # and model_fields_set contains the field
        if self.effective_aes_encryption_mode is None and "effective_aes_encryption_mode" in self.model_fields_set:
            _dict['effectiveAesEncryptionMode'] = None

        # set to None if is_auto_registered (nullable) is None
        # and model_fields_set contains the field
        if self.is_auto_registered is None and "is_auto_registered" in self.model_fields_set:
            _dict['isAutoRegistered'] = None

        # set to None if multi_tenancy_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.multi_tenancy_enabled is None and "multi_tenancy_enabled" in self.model_fields_set:
            _dict['multiTenancyEnabled'] = None

        # set to None if network_interface (nullable) is None
        # and model_fields_set contains the field
        if self.network_interface is None and "network_interface" in self.model_fields_set:
            _dict['networkInterface'] = None

        # set to None if purpose (nullable) is None
        # and model_fields_set contains the field
        if self.purpose is None and "purpose" in self.model_fields_set:
            _dict['purpose'] = None

        # set to None if supported_aes_encryption_mode (nullable) is None
        # and model_fields_set contains the field
        if self.supported_aes_encryption_mode is None and "supported_aes_encryption_mode" in self.model_fields_set:
            _dict['supportedAesEncryptionMode'] = None

        # set to None if tenant_storage_domain_sharing_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_storage_domain_sharing_enabled is None and "tenant_storage_domain_sharing_enabled" in self.model_fields_set:
            _dict['tenantStorageDomainSharingEnabled'] = None

        # set to None if tls_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.tls_enabled is None and "tls_enabled" in self.model_fields_set:
            _dict['tlsEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemoteClusterParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoRegisterTarget": obj.get("autoRegisterTarget") if obj.get("autoRegisterTarget") is not None else False,
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationId": obj.get("clusterIncarnationId"),
            "clusterName": obj.get("clusterName"),
            "description": obj.get("description"),
            "effectiveAesEncryptionMode": obj.get("effectiveAesEncryptionMode"),
            "isAutoRegistered": obj.get("isAutoRegistered"),
            "localAddresses": obj.get("localAddresses"),
            "multiTenancyEnabled": obj.get("multiTenancyEnabled"),
            "networkInterface": obj.get("networkInterface"),
            "purpose": obj.get("purpose"),
            "replicationParams": ReplicationParams.from_dict(obj["replicationParams"]) if obj.get("replicationParams") is not None else None,
            "supportedAesEncryptionMode": obj.get("supportedAesEncryptionMode"),
            "tenantStorageDomainSharingEnabled": obj.get("tenantStorageDomainSharingEnabled"),
            "tlsEnabled": obj.get("tlsEnabled")
        })
        return _obj


