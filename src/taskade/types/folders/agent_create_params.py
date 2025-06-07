# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AgentCreateParams",
    "Data",
    "DataUnionMember0",
    "DataUnionMember0Data",
    "DataUnionMember0DataCommand",
    "DataUnionMember0DataAvatar",
    "DataUnionMember0DataAvatarData",
    "DataUnionMember1",
    "DataUnionMember1Template",
    "DataUnionMember1TemplateAvatar",
    "DataUnionMember1TemplateAvatarData",
]


class AgentCreateParams(TypedDict, total=False):
    data: Required[Data]

    name: Required[str]


class DataUnionMember0DataCommand(TypedDict, total=False):
    id: Required[str]
    """ID based on the name in snake case."""

    name: Required[str]
    """Human-readable name of the command in title case.

    This should probably be a verb.
    """

    prompt: Required[str]
    """Tell the agent what this command will do.

    It should be positioned as a direct instruction to the agent. At least 30 words.
    """

    mode: Literal["default", "plan-and-execute-v1", "plan-and-execute-v2"]


class DataUnionMember0DataAvatarData(TypedDict, total=False):
    value: Required[str]
    """Pick the most suitable emoji for this agent."""


class DataUnionMember0DataAvatar(TypedDict, total=False):
    data: Required[DataUnionMember0DataAvatarData]

    type: Required[Literal["emoji"]]


class DataUnionMember0Data(TypedDict, total=False):
    commands: Required[Iterable[DataUnionMember0DataCommand]]

    avatar: DataUnionMember0DataAvatar

    description: str
    """Role and purpose of agent, positioned as a direct instruction to the agent.

    Example: "You are a doctor that helps save lives.". At least 100 words.
    """

    input_placeholder: Annotated[str, PropertyInfo(alias="inputPlaceholder")]

    knowledge_enabled: Annotated[bool, PropertyInfo(alias="knowledgeEnabled")]

    language: str
    """The language of the agent, e.g. en-US, zh-Hans"""

    tone: Literal[
        "authoritative",
        "clinical",
        "cold",
        "confident",
        "cynical",
        "emotional",
        "empathetic",
        "formal",
        "friendly",
        "humourous",
        "informal",
        "ironic",
        "optimistic",
        "pessimistic",
        "playful",
        "sarcastic",
        "serious",
        "sympathetic",
        "tentative",
        "warm",
        "creative",
        "inspiring",
        "casual",
    ]


class DataUnionMember0(TypedDict, total=False):
    data: Required[DataUnionMember0Data]

    type: Required[Literal["data"]]


class DataUnionMember1TemplateAvatarData(TypedDict, total=False):
    value: Required[str]
    """Pick the most suitable emoji for this agent."""


class DataUnionMember1TemplateAvatar(TypedDict, total=False):
    data: Required[DataUnionMember1TemplateAvatarData]

    type: Required[Literal["emoji"]]


class DataUnionMember1Template(TypedDict, total=False):
    type: Required[
        Literal[
            "Tasker",
            "Researcher",
            "Marketer",
            "EmailWriter",
            "Sales",
            "CustomerSupport",
            "ProjectManager",
            "ContentCreator",
            "Copywriter",
            "LegalAdvisor",
            "SeoSpecialist",
            "ProductivityCoach",
            "EngineeringExpert",
            "Translator",
            "Summarizer",
            "ResumeBuilder",
            "Storyteller",
            "Tutor",
            "BrandStrategist",
            "SocialMediaSpecialist",
            "BusinessStrategist",
            "FinancialAnalyst",
            "HumanResourcesManager",
            "DataScientist",
            "ITConsultant",
            "FinancialAdvisor",
            "HealthCoach",
            "SustainabilityConsultant",
            "UXDesigner",
            "QualityAssuranceAnalyst",
            "ProductManager",
            "GrowthHacker",
            "BusinessDevelopmentManager",
            "PublicRelationsSpecialist",
            "EventPlanner",
            "DataAnalyst",
            "Editor",
            "CEO",
            "InterviewCoach",
            "TechSupportAdvisor",
            "Doctor",
            "BlogExpert",
            "TweetOptimizer",
            "EmailMarketer",
            "CourseCreator",
            "ScriptCreator",
            "ScreenplayWriter",
            "Proofreader",
            "SalesColdEmailCoach",
            "CodeExplainer",
            "CreativeWritingCoach",
            "AdvertisingCopywriter",
            "VideoScriptWriter",
            "ProjectArchitect",
            "AICouncil",
            "Negotiator",
            "VCAssociate",
            "Books",
            "StartupMentor",
            "SmallBusiness",
            "WebDevelopment",
            "PromptEngineer",
            "ArticleWriter",
            "WorkflowAgent",
            "StrategyAgent",
            "ViralAgent",
            "SOPOnboardingAgent",
            "PressReleaseAgent",
        ]
    ]

    avatar: DataUnionMember1TemplateAvatar


class DataUnionMember1(TypedDict, total=False):
    template: Required[DataUnionMember1Template]

    type: Required[Literal["template"]]


Data: TypeAlias = Union[DataUnionMember0, DataUnionMember1]
