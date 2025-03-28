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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class UpgradeNotification(BaseModel):
    """
    Lists cluster upgrade notifications for an account.
    """ # noqa: E501
    is_upgrade_available: Optional[StrictBool] = Field(default=None, description="Specifies whether an upgrade is available for any of the clusters.", alias="isUpgradeAvailable")
    num_clusters_upgrade_available: Optional[StrictInt] = Field(default=None, description="Specifies the number of clusters with upgrade available.", alias="numClustersUpgradeAvailable")
    __properties: ClassVar[List[str]] = ["isUpgradeAvailable", "numClustersUpgradeAvailable"]

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
        """Create an instance of UpgradeNotification from a JSON string"""
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
        # set to None if is_upgrade_available (nullable) is None
        # and model_fields_set contains the field
        if self.is_upgrade_available is None and "is_upgrade_available" in self.model_fields_set:
            _dict['isUpgradeAvailable'] = None

        # set to None if num_clusters_upgrade_available (nullable) is None
        # and model_fields_set contains the field
        if self.num_clusters_upgrade_available is None and "num_clusters_upgrade_available" in self.model_fields_set:
            _dict['numClustersUpgradeAvailable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradeNotification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isUpgradeAvailable": obj.get("isUpgradeAvailable"),
            "numClustersUpgradeAvailable": obj.get("numClustersUpgradeAvailable")
        })
        return _obj


