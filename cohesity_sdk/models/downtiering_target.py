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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.downtiered_data_location import DowntieredDataLocation
from typing import Optional, Set
from typing_extensions import Self

class DowntieringTarget(BaseModel):
    """
    Specifies the target data tiering details for downtier job. This is in beta phase. Please use target inside CommonDataTieringTaskParams, present directly under data tiering request body. If target is present inside CommonDataTieringTaskParams, this target will be ignored.
    """ # noqa: E501
    downtiered_data_locations: Optional[List[Optional[DowntieredDataLocation]]] = Field(default=None, description="Specifies a list of mapping between sources and its corresponding viewNames and mountPaths, where the sources were downtiered.", alias="downtieredDataLocations")
    mount_path_prefix: Optional[StrictStr] = Field(default=None, description="Specifies the mount path prefix inside the view.", alias="mountPathPrefix")
    storage_domain_id: Optional[StrictInt] = Field(description="Specifies the Storage Domain ID where the view will be kept.", alias="storageDomainId")
    view_name_prefix: Optional[StrictStr] = Field(description="Specifies the view name prefix.", alias="viewNamePrefix")
    __properties: ClassVar[List[str]] = ["downtieredDataLocations", "mountPathPrefix", "storageDomainId", "viewNamePrefix"]

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
        """Create an instance of DowntieringTarget from a JSON string"""
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
            "downtiered_data_locations",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in downtiered_data_locations (list)
        _items = []
        if self.downtiered_data_locations:
            for _item_downtiered_data_locations in self.downtiered_data_locations:
                if _item_downtiered_data_locations:
                    _items.append(_item_downtiered_data_locations.to_dict())
            _dict['downtieredDataLocations'] = _items
        # set to None if downtiered_data_locations (nullable) is None
        # and model_fields_set contains the field
        if self.downtiered_data_locations is None and "downtiered_data_locations" in self.model_fields_set:
            _dict['downtieredDataLocations'] = None

        # set to None if mount_path_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.mount_path_prefix is None and "mount_path_prefix" in self.model_fields_set:
            _dict['mountPathPrefix'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if view_name_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.view_name_prefix is None and "view_name_prefix" in self.model_fields_set:
            _dict['viewNamePrefix'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DowntieringTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "downtieredDataLocations": [DowntieredDataLocation.from_dict(_item) for _item in obj["downtieredDataLocations"]] if obj.get("downtieredDataLocations") is not None else None,
            "mountPathPrefix": obj.get("mountPathPrefix"),
            "storageDomainId": obj.get("storageDomainId"),
            "viewNamePrefix": obj.get("viewNamePrefix")
        })
        return _obj


