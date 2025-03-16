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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Tag(BaseModel):
    """
    Tag details
    """ # noqa: E501
    created_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in microseconds since the epoch when this Tag was created.", alias="createdTimeUsecs")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Tag.")
    id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specifies unique id of the Tag.")
    last_updated_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in microseconds since the epoch when this Tag was last updated.", alias="lastUpdatedTimeUsecs")
    marked_for_deletion: Optional[StrictBool] = Field(default=None, description="If true, Tag is marked for deletion.", alias="markedForDeletion")
    name: Optional[StrictStr] = Field(description="Name of the Tag. Name has to be unique under Namespace.")
    namespace: Optional[StrictStr] = Field(description="Namespace of the Tag. This is used to filter tags based on application or usecase. For example all tags related to vcenter can be put under one namespace or different departments could have their own namespaces e.g. finance/tag1 or operations/tag2 etc.")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Tenant Id to whom the Tag belongs.", alias="tenantId")
    ui_color: Optional[StrictStr] = Field(default=None, description="Color of the tag in UI.", alias="uiColor")
    ui_path_elements: Optional[List[StrictStr]] = Field(default=None, description="Path of the tag for UI nesting purposes.", alias="uiPathElements")
    __properties: ClassVar[List[str]] = ["createdTimeUsecs", "description", "id", "lastUpdatedTimeUsecs", "markedForDeletion", "name", "namespace", "tenantId", "uiColor", "uiPathElements"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+:[A-Z0-9-]+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+:[A-Z0-9-]+$/")
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
        """Create an instance of Tag from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time_usecs",
            "id",
            "last_updated_time_usecs",
            "marked_for_deletion",
            "tenant_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if created_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_usecs is None and "created_time_usecs" in self.model_fields_set:
            _dict['createdTimeUsecs'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_updated_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time_usecs is None and "last_updated_time_usecs" in self.model_fields_set:
            _dict['lastUpdatedTimeUsecs'] = None

        # set to None if marked_for_deletion (nullable) is None
        # and model_fields_set contains the field
        if self.marked_for_deletion is None and "marked_for_deletion" in self.model_fields_set:
            _dict['markedForDeletion'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if ui_color (nullable) is None
        # and model_fields_set contains the field
        if self.ui_color is None and "ui_color" in self.model_fields_set:
            _dict['uiColor'] = None

        # set to None if ui_path_elements (nullable) is None
        # and model_fields_set contains the field
        if self.ui_path_elements is None and "ui_path_elements" in self.model_fields_set:
            _dict['uiPathElements'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Tag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdTimeUsecs": obj.get("createdTimeUsecs"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "lastUpdatedTimeUsecs": obj.get("lastUpdatedTimeUsecs"),
            "markedForDeletion": obj.get("markedForDeletion"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "tenantId": obj.get("tenantId"),
            "uiColor": obj.get("uiColor"),
            "uiPathElements": obj.get("uiPathElements")
        })
        return _obj


