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
from typing import Set
from typing_extensions import Self

class EntityIdentifiers(BaseModel):
    """
    Specifies the identifiers for an entity.
    """ # noqa: E501
    documentation_link: Optional[StrictStr] = Field(default=None, description="Specifies the link to documentation or additional information about the entity. This URL can be used to access more detailed information, guidelines, or metadata related to the entity id. It helps in understanding the context or usage of the entity id.", alias="documentationLink")
    key: Optional[StrictStr] = Field(default=None, description="Specifies the type of identifier. For example, a Virtual Machine (VM) can be identified through various types of IDs, such as UUID, Managed Object Reference (moref), or other unique identifiers.")
    value: Optional[StrictStr] = Field(default=None, description="Specifies the value of the identifier corresponding to the type specified in the key.")
    version: Optional[StrictInt] = Field(default=None, description="Specifies the version number associated with this EntityIdentifier")
    __properties: ClassVar[List[str]] = ["documentationLink", "key", "value", "version"]

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
        """Create an instance of EntityIdentifiers from a JSON string"""
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
        # set to None if documentation_link (nullable) is None
        # and model_fields_set contains the field
        if self.documentation_link is None and "documentation_link" in self.model_fields_set:
            _dict['documentationLink'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityIdentifiers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentationLink": obj.get("documentationLink"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "version": obj.get("version")
        })
        return _obj


