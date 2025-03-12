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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.key_value_pair import KeyValuePair
from typing import Optional, Set
from typing_extensions import Self

class CommonNoSqlRecoveryOptions(BaseModel):
    """
    Specifies the common properties required by all Nosl adapters at the time of recovery.
    """ # noqa: E501
    advanced_configs: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the advanced configuration for a recovery job.", alias="advancedConfigs")
    bandwidth_mbps: Optional[StrictInt] = Field(default=None, description="Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster.", alias="bandwidthMBPS")
    concurrency: Optional[StrictInt] = Field(default=None, description="Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster.")
    overwrite: Optional[StrictBool] = Field(default=None, description="Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object.")
    recover_to: Optional[StrictInt] = Field(default=None, description="Specifies the 'Source Registration ID' of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location.", alias="recoverTo")
    warnings: Optional[List[StrictStr]] = Field(default=None, description="This field will hold the warnings in cases where the job status is SucceededWithWarnings.")
    __properties: ClassVar[List[str]] = ["advancedConfigs", "bandwidthMBPS", "concurrency", "overwrite", "recoverTo", "warnings"]

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
        """Create an instance of CommonNoSqlRecoveryOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "warnings",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in advanced_configs (list)
        _items = []
        if self.advanced_configs:
            for _item_advanced_configs in self.advanced_configs:
                if _item_advanced_configs:
                    _items.append(_item_advanced_configs.to_dict())
            _dict['advancedConfigs'] = _items
        # set to None if advanced_configs (nullable) is None
        # and model_fields_set contains the field
        if self.advanced_configs is None and "advanced_configs" in self.model_fields_set:
            _dict['advancedConfigs'] = None

        # set to None if bandwidth_mbps (nullable) is None
        # and model_fields_set contains the field
        if self.bandwidth_mbps is None and "bandwidth_mbps" in self.model_fields_set:
            _dict['bandwidthMBPS'] = None

        # set to None if concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.concurrency is None and "concurrency" in self.model_fields_set:
            _dict['concurrency'] = None

        # set to None if overwrite (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite is None and "overwrite" in self.model_fields_set:
            _dict['overwrite'] = None

        # set to None if recover_to (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to is None and "recover_to" in self.model_fields_set:
            _dict['recoverTo'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonNoSqlRecoveryOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advancedConfigs": [KeyValuePair.from_dict(_item) for _item in obj["advancedConfigs"]] if obj.get("advancedConfigs") is not None else None,
            "bandwidthMBPS": obj.get("bandwidthMBPS"),
            "concurrency": obj.get("concurrency"),
            "overwrite": obj.get("overwrite"),
            "recoverTo": obj.get("recoverTo"),
            "warnings": obj.get("warnings")
        })
        return _obj


