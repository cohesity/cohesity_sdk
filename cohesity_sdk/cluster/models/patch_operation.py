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
from typing import Optional, Set
from typing_extensions import Self

class PatchOperation(BaseModel):
    """
    Specifies a patch operation.
    """ # noqa: E501
    component: Optional[StrictStr] = Field(default=None, description="Specifies the description of the service.")
    domain: Optional[StrictStr] = Field(default=None, description="Specifies the domain of the user.")
    operation: Optional[StrictStr] = Field(default=None, description="Specifies what patch management operation was performed")
    operation_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the patch operation was done in Unix epoch in milliseconds.", alias="operationTimeMsecs")
    service: Optional[StrictStr] = Field(default=None, description="Specifies the name of the service.")
    user: Optional[StrictStr] = Field(default=None, description="Specifies the user who performed the operation.")
    version: Optional[StrictStr] = Field(default=None, description="Specifies the version of the patch.")
    version_replaced: Optional[StrictStr] = Field(default=None, description="Specifies the version it replaced.", alias="versionReplaced")
    __properties: ClassVar[List[str]] = ["component", "domain", "operation", "operationTimeMsecs", "service", "user", "version", "versionReplaced"]

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
        """Create an instance of PatchOperation from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "component": obj.get("component"),
            "domain": obj.get("domain"),
            "operation": obj.get("operation"),
            "operationTimeMsecs": obj.get("operationTimeMsecs"),
            "service": obj.get("service"),
            "user": obj.get("user"),
            "version": obj.get("version"),
            "versionReplaced": obj.get("versionReplaced")
        })
        return _obj


