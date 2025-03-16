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
from cohesity_sdk.cluster.models.compression_params import CompressionParams
from cohesity_sdk.cluster.models.deduplication_params import DeduplicationParams
from cohesity_sdk.cluster.models.erasure_coding_params import ErasureCodingParams
from typing import Optional, Set
from typing_extensions import Self

class StoragePolicy(BaseModel):
    """
    Specifies the storage policy of a Storage Domain.
    """ # noqa: E501
    aes_encryption_mode: Optional[StrictStr] = Field(default=None, description="Specifies the encryption mode for a Storage Domain.", alias="aesEncryptionMode")
    app_marker_detection_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether app marker detection is enabled. When enabled, app markers will be removed from data and put in separate chunks.", alias="appMarkerDetectionEnabled")
    cloud_spill_vault_id: Optional[StrictInt] = Field(default=None, description="Specifies the vault id assigned for cloud spill for a Storage Domain.", alias="cloudSpillVaultId")
    compression_params: Optional[CompressionParams] = Field(default=None, alias="compressionParams")
    deduplication_compression_delay_secs: Optional[StrictInt] = Field(default=None, description="Specifies the time in seconds when deduplication and compression of the Storage Domain starts.", alias="deduplicationCompressionDelaySecs")
    deduplication_params: Optional[DeduplicationParams] = Field(default=None, alias="deduplicationParams")
    encryption_type: Optional[StrictStr] = Field(default=None, description="Specifies the encryption type for a Storage Domain.", alias="encryptionType")
    erasure_coding_params: Optional[ErasureCodingParams] = Field(default=None, alias="erasureCodingParams")
    num_disk_failures_tolerated: Optional[StrictInt] = Field(default=None, description="Specifies the number of disk failures to tolerate for a Storage Domain. By default, this field is 1 for cluster with three or more nodes. If erasure coding is enabled, this field will be the same as numCodedStripes.", alias="numDiskFailuresTolerated")
    num_node_failures_tolerated: Optional[StrictInt] = Field(default=None, description="Specifies the number of node failures to tolerate for a Storage Domain. By default this field is replication factor minus 1 for replication chunk files and is the same as numCodedStripes for erasure coding chunk files.", alias="numNodeFailuresTolerated")
    __properties: ClassVar[List[str]] = ["aesEncryptionMode", "appMarkerDetectionEnabled", "cloudSpillVaultId", "compressionParams", "deduplicationCompressionDelaySecs", "deduplicationParams", "encryptionType", "erasureCodingParams", "numDiskFailuresTolerated", "numNodeFailuresTolerated"]

    @field_validator('aes_encryption_mode')
    def aes_encryption_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CBC', 'GCM']):
            raise ValueError("must be one of enum values ('CBC', 'GCM')")
        return value

    @field_validator('encryption_type')
    def encryption_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Strong', 'Weak']):
            raise ValueError("must be one of enum values ('None', 'Strong', 'Weak')")
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
        """Create an instance of StoragePolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of compression_params
        if self.compression_params:
            _dict['compressionParams'] = self.compression_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deduplication_params
        if self.deduplication_params:
            _dict['deduplicationParams'] = self.deduplication_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of erasure_coding_params
        if self.erasure_coding_params:
            _dict['erasureCodingParams'] = self.erasure_coding_params.to_dict()
        # set to None if aes_encryption_mode (nullable) is None
        # and model_fields_set contains the field
        if self.aes_encryption_mode is None and "aes_encryption_mode" in self.model_fields_set:
            _dict['aesEncryptionMode'] = None

        # set to None if app_marker_detection_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.app_marker_detection_enabled is None and "app_marker_detection_enabled" in self.model_fields_set:
            _dict['appMarkerDetectionEnabled'] = None

        # set to None if cloud_spill_vault_id (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_spill_vault_id is None and "cloud_spill_vault_id" in self.model_fields_set:
            _dict['cloudSpillVaultId'] = None

        # set to None if deduplication_compression_delay_secs (nullable) is None
        # and model_fields_set contains the field
        if self.deduplication_compression_delay_secs is None and "deduplication_compression_delay_secs" in self.model_fields_set:
            _dict['deduplicationCompressionDelaySecs'] = None

        # set to None if encryption_type (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_type is None and "encryption_type" in self.model_fields_set:
            _dict['encryptionType'] = None

        # set to None if num_disk_failures_tolerated (nullable) is None
        # and model_fields_set contains the field
        if self.num_disk_failures_tolerated is None and "num_disk_failures_tolerated" in self.model_fields_set:
            _dict['numDiskFailuresTolerated'] = None

        # set to None if num_node_failures_tolerated (nullable) is None
        # and model_fields_set contains the field
        if self.num_node_failures_tolerated is None and "num_node_failures_tolerated" in self.model_fields_set:
            _dict['numNodeFailuresTolerated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StoragePolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aesEncryptionMode": obj.get("aesEncryptionMode"),
            "appMarkerDetectionEnabled": obj.get("appMarkerDetectionEnabled"),
            "cloudSpillVaultId": obj.get("cloudSpillVaultId"),
            "compressionParams": CompressionParams.from_dict(obj["compressionParams"]) if obj.get("compressionParams") is not None else None,
            "deduplicationCompressionDelaySecs": obj.get("deduplicationCompressionDelaySecs"),
            "deduplicationParams": DeduplicationParams.from_dict(obj["deduplicationParams"]) if obj.get("deduplicationParams") is not None else None,
            "encryptionType": obj.get("encryptionType"),
            "erasureCodingParams": ErasureCodingParams.from_dict(obj["erasureCodingParams"]) if obj.get("erasureCodingParams") is not None else None,
            "numDiskFailuresTolerated": obj.get("numDiskFailuresTolerated"),
            "numNodeFailuresTolerated": obj.get("numNodeFailuresTolerated")
        })
        return _obj


