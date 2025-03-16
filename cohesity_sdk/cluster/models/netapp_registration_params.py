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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.credentials import Credentials
from cohesity_sdk.cluster.models.filter_ip_config import FilterIpConfig
from cohesity_sdk.cluster.models.nas_throttling_config import NasThrottlingConfig
from cohesity_sdk.cluster.models.storage_array_snapshot_config import StorageArraySnapshotConfig
from typing import Optional, Set
from typing_extensions import Self

class NetappRegistrationParams(BaseModel):
    """
    Specifies parameters to register an Netapp Source.
    """ # noqa: E501
    back_up_smb_volumes: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to back up SMB Volumes.", alias="backUpSMBVolumes")
    credentials: Credentials
    endpoint: Optional[StrictStr] = Field(description="Specifies the Hostname or IP Address Endpoint for the Netapp Source.")
    filter_ip_config: Optional[FilterIpConfig] = Field(default=None, alias="filterIpConfig")
    smb_credentials: Optional[Credentials] = Field(default=None, alias="smbCredentials")
    source_type: Optional[StrictStr] = Field(description="Specifies the Netapp source type. Can be either kCluster or kVServer (SVM).", alias="sourceType")
    storage_array_snapshot_config: Optional[StorageArraySnapshotConfig] = Field(default=None, alias="storageArraySnapshotConfig")
    storage_array_snapshot_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if storage array snapshot is enabled or not in the Source.", alias="storageArraySnapshotEnabled")
    throttling_config: Optional[NasThrottlingConfig] = Field(default=None, alias="throttlingConfig")
    __properties: ClassVar[List[str]] = ["backUpSMBVolumes", "credentials", "endpoint", "filterIpConfig", "smbCredentials", "sourceType", "storageArraySnapshotConfig", "storageArraySnapshotEnabled", "throttlingConfig"]

    @field_validator('source_type')
    def source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kCluster', 'kVServer']):
            raise ValueError("must be one of enum values ('kCluster', 'kVServer')")
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
        """Create an instance of NetappRegistrationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter_ip_config
        if self.filter_ip_config:
            _dict['filterIpConfig'] = self.filter_ip_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smb_credentials
        if self.smb_credentials:
            _dict['smbCredentials'] = self.smb_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_array_snapshot_config
        if self.storage_array_snapshot_config:
            _dict['storageArraySnapshotConfig'] = self.storage_array_snapshot_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throttling_config
        if self.throttling_config:
            _dict['throttlingConfig'] = self.throttling_config.to_dict()
        # set to None if back_up_smb_volumes (nullable) is None
        # and model_fields_set contains the field
        if self.back_up_smb_volumes is None and "back_up_smb_volumes" in self.model_fields_set:
            _dict['backUpSMBVolumes'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if source_type (nullable) is None
        # and model_fields_set contains the field
        if self.source_type is None and "source_type" in self.model_fields_set:
            _dict['sourceType'] = None

        # set to None if storage_array_snapshot_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.storage_array_snapshot_enabled is None and "storage_array_snapshot_enabled" in self.model_fields_set:
            _dict['storageArraySnapshotEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetappRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backUpSMBVolumes": obj.get("backUpSMBVolumes"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "endpoint": obj.get("endpoint"),
            "filterIpConfig": FilterIpConfig.from_dict(obj["filterIpConfig"]) if obj.get("filterIpConfig") is not None else None,
            "smbCredentials": Credentials.from_dict(obj["smbCredentials"]) if obj.get("smbCredentials") is not None else None,
            "sourceType": obj.get("sourceType"),
            "storageArraySnapshotConfig": StorageArraySnapshotConfig.from_dict(obj["storageArraySnapshotConfig"]) if obj.get("storageArraySnapshotConfig") is not None else None,
            "storageArraySnapshotEnabled": obj.get("storageArraySnapshotEnabled"),
            "throttlingConfig": NasThrottlingConfig.from_dict(obj["throttlingConfig"]) if obj.get("throttlingConfig") is not None else None
        })
        return _obj


