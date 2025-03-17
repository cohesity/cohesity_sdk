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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class ReleaseDownloadUrls(BaseModel):
    """
    Different types of release urls.
    """ # noqa: E501
    deliverable_type: Optional[StrictStr] = Field(default=None, description="Specifies url type.", alias="deliverableType")
    docs: Optional[StrictStr] = Field(default=None, description="Specifies url doc link.")
    fast_link: Optional[StrictStr] = Field(default=None, description="Specifies url fast link.", alias="fastLink")
    fixed_issues_link: Optional[StrictStr] = Field(default=None, description="Specifies url doc link containing description for release.", alias="fixedIssuesLink")
    md5_check_sum: Optional[StrictStr] = Field(default=None, description="Specifies url checksum.", alias="md5CheckSum")
    mirror_link: Optional[StrictStr] = Field(default=None, description="Specifies url mirror link.", alias="mirrorLink")
    what_is_new_link: Optional[StrictStr] = Field(default=None, description="Specifies url doc link containing description for release.", alias="whatIsNewLink")
    __properties: ClassVar[List[str]] = ["deliverableType", "docs", "fastLink", "fixedIssuesLink", "md5CheckSum", "mirrorLink", "whatIsNewLink"]

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
        """Create an instance of ReleaseDownloadUrls from a JSON string"""
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
        # set to None if deliverable_type (nullable) is None
        # and model_fields_set contains the field
        if self.deliverable_type is None and "deliverable_type" in self.model_fields_set:
            _dict['deliverableType'] = None

        # set to None if docs (nullable) is None
        # and model_fields_set contains the field
        if self.docs is None and "docs" in self.model_fields_set:
            _dict['docs'] = None

        # set to None if fast_link (nullable) is None
        # and model_fields_set contains the field
        if self.fast_link is None and "fast_link" in self.model_fields_set:
            _dict['fastLink'] = None

        # set to None if fixed_issues_link (nullable) is None
        # and model_fields_set contains the field
        if self.fixed_issues_link is None and "fixed_issues_link" in self.model_fields_set:
            _dict['fixedIssuesLink'] = None

        # set to None if md5_check_sum (nullable) is None
        # and model_fields_set contains the field
        if self.md5_check_sum is None and "md5_check_sum" in self.model_fields_set:
            _dict['md5CheckSum'] = None

        # set to None if mirror_link (nullable) is None
        # and model_fields_set contains the field
        if self.mirror_link is None and "mirror_link" in self.model_fields_set:
            _dict['mirrorLink'] = None

        # set to None if what_is_new_link (nullable) is None
        # and model_fields_set contains the field
        if self.what_is_new_link is None and "what_is_new_link" in self.model_fields_set:
            _dict['whatIsNewLink'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReleaseDownloadUrls from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliverableType": obj.get("deliverableType"),
            "docs": obj.get("docs"),
            "fastLink": obj.get("fastLink"),
            "fixedIssuesLink": obj.get("fixedIssuesLink"),
            "md5CheckSum": obj.get("md5CheckSum"),
            "mirrorLink": obj.get("mirrorLink"),
            "whatIsNewLink": obj.get("whatIsNewLink")
        })
        return _obj


