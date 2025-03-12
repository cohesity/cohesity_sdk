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
from cohesity_sdk.helios.models.vault_transfer_time_config import VaultTransferTimeConfig
from typing import Set
from typing_extensions import Self

class VaultTransferTimeConfigs(BaseModel):
    """
    List of FortKnox vaults transfer time configurations.
    """ # noqa: E501
    transfer_time_configs: Optional[List[VaultTransferTimeConfig]] = Field(default=None, description="List of FortKnox vaults transfer time configurations.", alias="transferTimeConfigs")
    __properties: ClassVar[List[str]] = ["transferTimeConfigs"]

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
        """Create an instance of VaultTransferTimeConfigs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transfer_time_configs (list)
        _items = []
        if self.transfer_time_configs:
            for _item_transfer_time_configs in self.transfer_time_configs:
                if _item_transfer_time_configs:
                    _items.append(_item_transfer_time_configs.to_dict())
            _dict['transferTimeConfigs'] = _items
        # set to None if transfer_time_configs (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_time_configs is None and "transfer_time_configs" in self.model_fields_set:
            _dict['transferTimeConfigs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VaultTransferTimeConfigs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transferTimeConfigs": [VaultTransferTimeConfig.from_dict(_item) for _item in obj["transferTimeConfigs"]] if obj.get("transferTimeConfigs") is not None else None
        })
        return _obj


