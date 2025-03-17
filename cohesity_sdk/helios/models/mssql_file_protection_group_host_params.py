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
from typing import Set
from typing_extensions import Self

class MSSQLFileProtectionGroupHostParams(BaseModel):
    """
    Specifies the host specific parameters for a host container in this protection group. Objects specified here should only be MSSQL root containers and will not be protected unless they are also specified in the 'objects' list. This list is just for specifying source level settings.
    """ # noqa: E501
    disable_source_side_deduplication: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to disable source side deduplication on this source. The default behavior is false unless the user has set 'performSourceSideDeduplication' to true.", alias="disableSourceSideDeduplication")
    host_id: Optional[StrictInt] = Field(description="Specifies the id of the host container on which databases are hosted.", alias="hostId")
    host_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the host container on which databases are hosted.", alias="hostName")
    __properties: ClassVar[List[str]] = ["disableSourceSideDeduplication", "hostId", "hostName"]

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
        """Create an instance of MSSQLFileProtectionGroupHostParams from a JSON string"""
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
            "host_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if disable_source_side_deduplication (nullable) is None
        # and model_fields_set contains the field
        if self.disable_source_side_deduplication is None and "disable_source_side_deduplication" in self.model_fields_set:
            _dict['disableSourceSideDeduplication'] = None

        # set to None if host_id (nullable) is None
        # and model_fields_set contains the field
        if self.host_id is None and "host_id" in self.model_fields_set:
            _dict['hostId'] = None

        # set to None if host_name (nullable) is None
        # and model_fields_set contains the field
        if self.host_name is None and "host_name" in self.model_fields_set:
            _dict['hostName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MSSQLFileProtectionGroupHostParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disableSourceSideDeduplication": obj.get("disableSourceSideDeduplication"),
            "hostId": obj.get("hostId"),
            "hostName": obj.get("hostName")
        })
        return _obj


