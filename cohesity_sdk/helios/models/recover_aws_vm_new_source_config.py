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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.encryption_config import EncryptionConfig
from cohesity_sdk.helios.models.recover_aws_vm_new_source_network_config import RecoverAwsVmNewSourceNetworkConfig
from cohesity_sdk.helios.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class RecoverAwsVmNewSourceConfig(BaseModel):
    """
    Specifies the new destination Source configuration where the VMs will be recovered.
    """ # noqa: E501
    encryption_config: Optional[EncryptionConfig] = Field(default=None, alias="encryptionConfig")
    key_pair: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="keyPair")
    network_config: RecoverAwsVmNewSourceNetworkConfig = Field(alias="networkConfig")
    region: RecoveryObjectIdentifier
    source: RecoveryObjectIdentifier
    __properties: ClassVar[List[str]] = ["encryptionConfig", "keyPair", "networkConfig", "region", "source"]

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
        """Create an instance of RecoverAwsVmNewSourceConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of encryption_config
        if self.encryption_config:
            _dict['encryptionConfig'] = self.encryption_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of key_pair
        if self.key_pair:
            _dict['keyPair'] = self.key_pair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_config
        if self.network_config:
            _dict['networkConfig'] = self.network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAwsVmNewSourceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "encryptionConfig": EncryptionConfig.from_dict(obj["encryptionConfig"]) if obj.get("encryptionConfig") is not None else None,
            "keyPair": RecoveryObjectIdentifier.from_dict(obj["keyPair"]) if obj.get("keyPair") is not None else None,
            "networkConfig": RecoverAwsVmNewSourceNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "region": RecoveryObjectIdentifier.from_dict(obj["region"]) if obj.get("region") is not None else None,
            "source": RecoveryObjectIdentifier.from_dict(obj["source"]) if obj.get("source") is not None else None
        })
        return _obj


