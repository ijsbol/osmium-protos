import auth_pb2 as _auth_pb2
import messages_pb2 as _messages_pb2
import chats_pb2 as _chats_pb2
import updates_pb2 as _updates_pb2
import friends_pb2 as _friends_pb2
import communities_pb2 as _communities_pb2
import media_pb2 as _media_pb2
import types_pb2 as _types_pb2
import settings_pb2 as _settings_pb2
import voice_pb2 as _voice_pb2
import users_pb2 as _users_pb2
import reactions_pb2 as _reactions_pb2
import stickers_pb2 as _stickers_pb2
import billing_pb2 as _billing_pb2
import discovery_pb2 as _discovery_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientMessage(_message.Message):
    __slots__ = ("id", "auth_sign_in", "auth_sign_up", "messages_send_message", "messages_get_history", "communities_create_community", "communities_get_communities", "communities_create_channel", "communities_get_channels", "friends_get_relationships", "chats_get_chats", "media_upload_file_part", "media_download_file_part", "chats_create_chat_invite", "auth_lookup_invite", "auth_use_invite", "messages_delete_message", "communities_get_channel_members", "core_initialize", "auth_authorize", "chats_mark_chat_read", "settings_edit_profile_photo", "communities_edit_photo", "communities_delete_channel", "chats_get_chat", "messages_edit_message", "communities_get_roles", "chats_set_typing", "communities_create_role", "communities_edit_role", "communities_delete_role", "communities_edit_member", "communities_create_channel_override", "communities_delete_channel_override", "communities_get_channel_overrides", "communities_leave_community", "communities_delete_community", "friends_sync_friends", "communities_edit_channel", "communities_edit_community", "auth_get_sessions", "auth_revoke_sessions", "settings_register_push_subscription", "settings_unregister_push_subscription", "auth_reset_password", "auth_verify_email", "auth_resend_email_verification", "users_lookup_username", "communities_remove_members", "chats_create_chat", "friends_change_relationship", "chats_update_chat", "chats_remove_chat_member", "voice_request_room", "messages_search", "messages_get_embed_preview", "users_get_profile", "communities_edit_default_permissions", "chats_delete_chat_invite", "communities_get_removed_members", "chats_list_chat_invites", "messages_report_message", "reactions_add_reaction", "reactions_remove_reaction", "messages_forward_message", "stickers_get_saved_stickers", "stickers_get_sticker_files", "stickers_get_sticker_pack", "stickers_add_sticker_to_pack", "stickers_remove_sticker_from_pack", "billing_request_payment_link", "billing_cancel_subscription", "settings_change_notification_preferences", "settings_edit_profile", "settings_get_account", "settings_change_password", "settings_change_email", "communities_unban_members", "communities_get_members", "settings_change_status", "communities_edit_settings", "billing_get_subscription", "settings_setup_totp", "settings_request_takeout", "settings_delete_account", "messages_get_unread_mentions", "discovery_get_discoverable_communities", "communities_get_room_states", "messages_set_message_pin", "messages_get_pinned_messages", "settings_edit_user_settings")
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_SIGN_IN_FIELD_NUMBER: _ClassVar[int]
    AUTH_SIGN_UP_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_GET_HISTORY_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_CREATE_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_CREATE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_GET_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    CHATS_GET_CHATS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_UPLOAD_FILE_PART_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DOWNLOAD_FILE_PART_FIELD_NUMBER: _ClassVar[int]
    CHATS_CREATE_CHAT_INVITE_FIELD_NUMBER: _ClassVar[int]
    AUTH_LOOKUP_INVITE_FIELD_NUMBER: _ClassVar[int]
    AUTH_USE_INVITE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_CHANNEL_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CORE_INITIALIZE_FIELD_NUMBER: _ClassVar[int]
    AUTH_AUTHORIZE_FIELD_NUMBER: _ClassVar[int]
    CHATS_MARK_CHAT_READ_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_EDIT_PROFILE_PHOTO_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_PHOTO_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_DELETE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHATS_GET_CHAT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_EDIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_ROLES_FIELD_NUMBER: _ClassVar[int]
    CHATS_SET_TYPING_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_CREATE_ROLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_ROLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_DELETE_ROLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_CREATE_CHANNEL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_DELETE_CHANNEL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_CHANNEL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_LEAVE_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_DELETE_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_SYNC_FRIENDS_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    AUTH_GET_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    AUTH_REVOKE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_REGISTER_PUSH_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_UNREGISTER_PUSH_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTH_RESET_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    AUTH_VERIFY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AUTH_RESEND_EMAIL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    USERS_LOOKUP_USERNAME_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_REMOVE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHATS_CREATE_CHAT_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_CHANGE_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    CHATS_UPDATE_CHAT_FIELD_NUMBER: _ClassVar[int]
    CHATS_REMOVE_CHAT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    VOICE_REQUEST_ROOM_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_SEARCH_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_GET_EMBED_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    USERS_GET_PROFILE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CHATS_DELETE_CHAT_INVITE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_REMOVED_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHATS_LIST_CHAT_INVITES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_REPORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_ADD_REACTION_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_REMOVE_REACTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FORWARD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STICKERS_GET_SAVED_STICKERS_FIELD_NUMBER: _ClassVar[int]
    STICKERS_GET_STICKER_FILES_FIELD_NUMBER: _ClassVar[int]
    STICKERS_GET_STICKER_PACK_FIELD_NUMBER: _ClassVar[int]
    STICKERS_ADD_STICKER_TO_PACK_FIELD_NUMBER: _ClassVar[int]
    STICKERS_REMOVE_STICKER_FROM_PACK_FIELD_NUMBER: _ClassVar[int]
    BILLING_REQUEST_PAYMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    BILLING_CANCEL_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGE_NOTIFICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_EDIT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_GET_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGE_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_UNBAN_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_EDIT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BILLING_GET_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_SETUP_TOTP_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_REQUEST_TAKEOUT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_DELETE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_GET_UNREAD_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_GET_DISCOVERABLE_COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_GET_ROOM_STATES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_SET_MESSAGE_PIN_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_GET_PINNED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_EDIT_USER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    auth_sign_in: _auth_pb2.SignIn
    auth_sign_up: _auth_pb2.SignUp
    messages_send_message: _messages_pb2.SendMessage
    messages_get_history: _messages_pb2.GetHistory
    communities_create_community: _communities_pb2.CreateCommunity
    communities_get_communities: _communities_pb2.GetCommunities
    communities_create_channel: _communities_pb2.CreateChannel
    communities_get_channels: _communities_pb2.GetChannels
    friends_get_relationships: _friends_pb2.GetRelationships
    chats_get_chats: _chats_pb2.GetChats
    media_upload_file_part: _media_pb2.UploadFilePart
    media_download_file_part: _media_pb2.DownloadFilePart
    chats_create_chat_invite: _chats_pb2.CreateChatInvite
    auth_lookup_invite: _auth_pb2.LookupInvite
    auth_use_invite: _auth_pb2.UseInvite
    messages_delete_message: _messages_pb2.DeleteMessage
    communities_get_channel_members: _communities_pb2.GetChannelMembers
    core_initialize: Initialize
    auth_authorize: _auth_pb2.Authorize
    chats_mark_chat_read: _chats_pb2.MarkChatRead
    settings_edit_profile_photo: _settings_pb2.EditProfilePhoto
    communities_edit_photo: _communities_pb2.EditPhoto
    communities_delete_channel: _communities_pb2.DeleteChannel
    chats_get_chat: _chats_pb2.GetChat
    messages_edit_message: _messages_pb2.EditMessage
    communities_get_roles: _communities_pb2.GetRoles
    chats_set_typing: _chats_pb2.SetTyping
    communities_create_role: _communities_pb2.CreateRole
    communities_edit_role: _communities_pb2.EditRole
    communities_delete_role: _communities_pb2.DeleteRole
    communities_edit_member: _communities_pb2.EditMember
    communities_create_channel_override: _communities_pb2.CreateChannelOverride
    communities_delete_channel_override: _communities_pb2.DeleteChannelOverride
    communities_get_channel_overrides: _communities_pb2.GetChannelOverrides
    communities_leave_community: _communities_pb2.LeaveCommunity
    communities_delete_community: _communities_pb2.DeleteCommunity
    friends_sync_friends: _friends_pb2.SyncFriends
    communities_edit_channel: _communities_pb2.EditChannel
    communities_edit_community: _communities_pb2.EditCommunity
    auth_get_sessions: _auth_pb2.GetSessions
    auth_revoke_sessions: _auth_pb2.RevokeSessions
    settings_register_push_subscription: _settings_pb2.RegisterPushSubscription
    settings_unregister_push_subscription: _settings_pb2.UnregisterPushSubscription
    auth_reset_password: _auth_pb2.ResetPassword
    auth_verify_email: _auth_pb2.VerifyEmail
    auth_resend_email_verification: _auth_pb2.ResendEmailVerification
    users_lookup_username: _users_pb2.LookupUsername
    communities_remove_members: _communities_pb2.RemoveMembers
    chats_create_chat: _chats_pb2.CreateChat
    friends_change_relationship: _friends_pb2.ChangeRelationship
    chats_update_chat: _chats_pb2.UpdateChat
    chats_remove_chat_member: _chats_pb2.RemoveChatMember
    voice_request_room: _voice_pb2.RequestRoom
    messages_search: _messages_pb2.Search
    messages_get_embed_preview: _messages_pb2.GetEmbedPreview
    users_get_profile: _users_pb2.GetProfile
    communities_edit_default_permissions: _communities_pb2.EditDefaultPermissions
    chats_delete_chat_invite: _chats_pb2.DeleteChatInvite
    communities_get_removed_members: _communities_pb2.GetRemovedMembers
    chats_list_chat_invites: _chats_pb2.ListChatInvites
    messages_report_message: _messages_pb2.ReportMessage
    reactions_add_reaction: _reactions_pb2.AddReaction
    reactions_remove_reaction: _reactions_pb2.RemoveReaction
    messages_forward_message: _messages_pb2.ForwardMessage
    stickers_get_saved_stickers: _stickers_pb2.GetSavedStickers
    stickers_get_sticker_files: _stickers_pb2.GetStickerFiles
    stickers_get_sticker_pack: _stickers_pb2.GetStickerPack
    stickers_add_sticker_to_pack: _stickers_pb2.AddStickerToPack
    stickers_remove_sticker_from_pack: _stickers_pb2.RemoveStickerFromPack
    billing_request_payment_link: _billing_pb2.RequestPaymentLink
    billing_cancel_subscription: _billing_pb2.CancelSubscription
    settings_change_notification_preferences: _settings_pb2.ChangeNotificationPreferences
    settings_edit_profile: _settings_pb2.EditProfile
    settings_get_account: _settings_pb2.GetAccount
    settings_change_password: _settings_pb2.ChangePassword
    settings_change_email: _settings_pb2.ChangeEmail
    communities_unban_members: _communities_pb2.UnbanMembers
    communities_get_members: _communities_pb2.GetMembers
    settings_change_status: _settings_pb2.ChangeStatus
    communities_edit_settings: _communities_pb2.EditSettings
    billing_get_subscription: _billing_pb2.GetSubscription
    settings_setup_totp: _settings_pb2.SetupTotp
    settings_request_takeout: _settings_pb2.RequestTakeout
    settings_delete_account: _settings_pb2.DeleteAccount
    messages_get_unread_mentions: _messages_pb2.GetUnreadMentions
    discovery_get_discoverable_communities: _discovery_pb2.GetDiscoverableCommunities
    communities_get_room_states: _communities_pb2.GetRoomStates
    messages_set_message_pin: _messages_pb2.SetMessagePin
    messages_get_pinned_messages: _messages_pb2.GetPinnedMessages
    settings_edit_user_settings: _settings_pb2.EditUserSettings
    def __init__(self, id: _Optional[int] = ..., auth_sign_in: _Optional[_Union[_auth_pb2.SignIn, _Mapping]] = ..., auth_sign_up: _Optional[_Union[_auth_pb2.SignUp, _Mapping]] = ..., messages_send_message: _Optional[_Union[_messages_pb2.SendMessage, _Mapping]] = ..., messages_get_history: _Optional[_Union[_messages_pb2.GetHistory, _Mapping]] = ..., communities_create_community: _Optional[_Union[_communities_pb2.CreateCommunity, _Mapping]] = ..., communities_get_communities: _Optional[_Union[_communities_pb2.GetCommunities, _Mapping]] = ..., communities_create_channel: _Optional[_Union[_communities_pb2.CreateChannel, _Mapping]] = ..., communities_get_channels: _Optional[_Union[_communities_pb2.GetChannels, _Mapping]] = ..., friends_get_relationships: _Optional[_Union[_friends_pb2.GetRelationships, _Mapping]] = ..., chats_get_chats: _Optional[_Union[_chats_pb2.GetChats, _Mapping]] = ..., media_upload_file_part: _Optional[_Union[_media_pb2.UploadFilePart, _Mapping]] = ..., media_download_file_part: _Optional[_Union[_media_pb2.DownloadFilePart, _Mapping]] = ..., chats_create_chat_invite: _Optional[_Union[_chats_pb2.CreateChatInvite, _Mapping]] = ..., auth_lookup_invite: _Optional[_Union[_auth_pb2.LookupInvite, _Mapping]] = ..., auth_use_invite: _Optional[_Union[_auth_pb2.UseInvite, _Mapping]] = ..., messages_delete_message: _Optional[_Union[_messages_pb2.DeleteMessage, _Mapping]] = ..., communities_get_channel_members: _Optional[_Union[_communities_pb2.GetChannelMembers, _Mapping]] = ..., core_initialize: _Optional[_Union[Initialize, _Mapping]] = ..., auth_authorize: _Optional[_Union[_auth_pb2.Authorize, _Mapping]] = ..., chats_mark_chat_read: _Optional[_Union[_chats_pb2.MarkChatRead, _Mapping]] = ..., settings_edit_profile_photo: _Optional[_Union[_settings_pb2.EditProfilePhoto, _Mapping]] = ..., communities_edit_photo: _Optional[_Union[_communities_pb2.EditPhoto, _Mapping]] = ..., communities_delete_channel: _Optional[_Union[_communities_pb2.DeleteChannel, _Mapping]] = ..., chats_get_chat: _Optional[_Union[_chats_pb2.GetChat, _Mapping]] = ..., messages_edit_message: _Optional[_Union[_messages_pb2.EditMessage, _Mapping]] = ..., communities_get_roles: _Optional[_Union[_communities_pb2.GetRoles, _Mapping]] = ..., chats_set_typing: _Optional[_Union[_chats_pb2.SetTyping, _Mapping]] = ..., communities_create_role: _Optional[_Union[_communities_pb2.CreateRole, _Mapping]] = ..., communities_edit_role: _Optional[_Union[_communities_pb2.EditRole, _Mapping]] = ..., communities_delete_role: _Optional[_Union[_communities_pb2.DeleteRole, _Mapping]] = ..., communities_edit_member: _Optional[_Union[_communities_pb2.EditMember, _Mapping]] = ..., communities_create_channel_override: _Optional[_Union[_communities_pb2.CreateChannelOverride, _Mapping]] = ..., communities_delete_channel_override: _Optional[_Union[_communities_pb2.DeleteChannelOverride, _Mapping]] = ..., communities_get_channel_overrides: _Optional[_Union[_communities_pb2.GetChannelOverrides, _Mapping]] = ..., communities_leave_community: _Optional[_Union[_communities_pb2.LeaveCommunity, _Mapping]] = ..., communities_delete_community: _Optional[_Union[_communities_pb2.DeleteCommunity, _Mapping]] = ..., friends_sync_friends: _Optional[_Union[_friends_pb2.SyncFriends, _Mapping]] = ..., communities_edit_channel: _Optional[_Union[_communities_pb2.EditChannel, _Mapping]] = ..., communities_edit_community: _Optional[_Union[_communities_pb2.EditCommunity, _Mapping]] = ..., auth_get_sessions: _Optional[_Union[_auth_pb2.GetSessions, _Mapping]] = ..., auth_revoke_sessions: _Optional[_Union[_auth_pb2.RevokeSessions, _Mapping]] = ..., settings_register_push_subscription: _Optional[_Union[_settings_pb2.RegisterPushSubscription, _Mapping]] = ..., settings_unregister_push_subscription: _Optional[_Union[_settings_pb2.UnregisterPushSubscription, _Mapping]] = ..., auth_reset_password: _Optional[_Union[_auth_pb2.ResetPassword, _Mapping]] = ..., auth_verify_email: _Optional[_Union[_auth_pb2.VerifyEmail, _Mapping]] = ..., auth_resend_email_verification: _Optional[_Union[_auth_pb2.ResendEmailVerification, _Mapping]] = ..., users_lookup_username: _Optional[_Union[_users_pb2.LookupUsername, _Mapping]] = ..., communities_remove_members: _Optional[_Union[_communities_pb2.RemoveMembers, _Mapping]] = ..., chats_create_chat: _Optional[_Union[_chats_pb2.CreateChat, _Mapping]] = ..., friends_change_relationship: _Optional[_Union[_friends_pb2.ChangeRelationship, _Mapping]] = ..., chats_update_chat: _Optional[_Union[_chats_pb2.UpdateChat, _Mapping]] = ..., chats_remove_chat_member: _Optional[_Union[_chats_pb2.RemoveChatMember, _Mapping]] = ..., voice_request_room: _Optional[_Union[_voice_pb2.RequestRoom, _Mapping]] = ..., messages_search: _Optional[_Union[_messages_pb2.Search, _Mapping]] = ..., messages_get_embed_preview: _Optional[_Union[_messages_pb2.GetEmbedPreview, _Mapping]] = ..., users_get_profile: _Optional[_Union[_users_pb2.GetProfile, _Mapping]] = ..., communities_edit_default_permissions: _Optional[_Union[_communities_pb2.EditDefaultPermissions, _Mapping]] = ..., chats_delete_chat_invite: _Optional[_Union[_chats_pb2.DeleteChatInvite, _Mapping]] = ..., communities_get_removed_members: _Optional[_Union[_communities_pb2.GetRemovedMembers, _Mapping]] = ..., chats_list_chat_invites: _Optional[_Union[_chats_pb2.ListChatInvites, _Mapping]] = ..., messages_report_message: _Optional[_Union[_messages_pb2.ReportMessage, _Mapping]] = ..., reactions_add_reaction: _Optional[_Union[_reactions_pb2.AddReaction, _Mapping]] = ..., reactions_remove_reaction: _Optional[_Union[_reactions_pb2.RemoveReaction, _Mapping]] = ..., messages_forward_message: _Optional[_Union[_messages_pb2.ForwardMessage, _Mapping]] = ..., stickers_get_saved_stickers: _Optional[_Union[_stickers_pb2.GetSavedStickers, _Mapping]] = ..., stickers_get_sticker_files: _Optional[_Union[_stickers_pb2.GetStickerFiles, _Mapping]] = ..., stickers_get_sticker_pack: _Optional[_Union[_stickers_pb2.GetStickerPack, _Mapping]] = ..., stickers_add_sticker_to_pack: _Optional[_Union[_stickers_pb2.AddStickerToPack, _Mapping]] = ..., stickers_remove_sticker_from_pack: _Optional[_Union[_stickers_pb2.RemoveStickerFromPack, _Mapping]] = ..., billing_request_payment_link: _Optional[_Union[_billing_pb2.RequestPaymentLink, _Mapping]] = ..., billing_cancel_subscription: _Optional[_Union[_billing_pb2.CancelSubscription, _Mapping]] = ..., settings_change_notification_preferences: _Optional[_Union[_settings_pb2.ChangeNotificationPreferences, _Mapping]] = ..., settings_edit_profile: _Optional[_Union[_settings_pb2.EditProfile, _Mapping]] = ..., settings_get_account: _Optional[_Union[_settings_pb2.GetAccount, _Mapping]] = ..., settings_change_password: _Optional[_Union[_settings_pb2.ChangePassword, _Mapping]] = ..., settings_change_email: _Optional[_Union[_settings_pb2.ChangeEmail, _Mapping]] = ..., communities_unban_members: _Optional[_Union[_communities_pb2.UnbanMembers, _Mapping]] = ..., communities_get_members: _Optional[_Union[_communities_pb2.GetMembers, _Mapping]] = ..., settings_change_status: _Optional[_Union[_settings_pb2.ChangeStatus, _Mapping]] = ..., communities_edit_settings: _Optional[_Union[_communities_pb2.EditSettings, _Mapping]] = ..., billing_get_subscription: _Optional[_Union[_billing_pb2.GetSubscription, _Mapping]] = ..., settings_setup_totp: _Optional[_Union[_settings_pb2.SetupTotp, _Mapping]] = ..., settings_request_takeout: _Optional[_Union[_settings_pb2.RequestTakeout, _Mapping]] = ..., settings_delete_account: _Optional[_Union[_settings_pb2.DeleteAccount, _Mapping]] = ..., messages_get_unread_mentions: _Optional[_Union[_messages_pb2.GetUnreadMentions, _Mapping]] = ..., discovery_get_discoverable_communities: _Optional[_Union[_discovery_pb2.GetDiscoverableCommunities, _Mapping]] = ..., communities_get_room_states: _Optional[_Union[_communities_pb2.GetRoomStates, _Mapping]] = ..., messages_set_message_pin: _Optional[_Union[_messages_pb2.SetMessagePin, _Mapping]] = ..., messages_get_pinned_messages: _Optional[_Union[_messages_pb2.GetPinnedMessages, _Mapping]] = ..., settings_edit_user_settings: _Optional[_Union[_settings_pb2.EditUserSettings, _Mapping]] = ...) -> None: ...

class ServerMessage(_message.Message):
    __slots__ = ("id", "update", "result")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    update: _updates_pb2.Update
    result: RPCResult
    def __init__(self, id: _Optional[int] = ..., update: _Optional[_Union[_updates_pb2.Update, _Mapping]] = ..., result: _Optional[_Union[RPCResult, _Mapping]] = ...) -> None: ...

class RPCResult(_message.Message):
    __slots__ = ("req_id", "trace_id", "error", "sent_message", "authorization", "communities", "channels", "messages", "relationships", "chats", "file_part", "created_invite", "member_list", "initialized", "chat", "community_roles", "channel_override", "channel_overrides", "sessions", "user_details", "removed_members", "group", "invite_preview", "room_info", "media_embed", "profile", "invite_list", "saved_stickers", "files", "sticker_pack", "payment_link", "account", "members", "community_settings", "subscription", "totp", "unread_mentions", "discovery_communities", "room_states", "user_settings")
    REQ_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    CHATS_FIELD_NUMBER: _ClassVar[int]
    FILE_PART_FIELD_NUMBER: _ClassVar[int]
    CREATED_INVITE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ROLES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    INVITE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    ROOM_INFO_FIELD_NUMBER: _ClassVar[int]
    MEDIA_EMBED_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    INVITE_LIST_FIELD_NUMBER: _ClassVar[int]
    SAVED_STICKERS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    STICKER_PACK_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOTP_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_COMMUNITIES_FIELD_NUMBER: _ClassVar[int]
    ROOM_STATES_FIELD_NUMBER: _ClassVar[int]
    USER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    req_id: int
    trace_id: str
    error: RPCError
    sent_message: _messages_pb2.SentMessage
    authorization: _auth_pb2.Authorization
    communities: _communities_pb2.Communities
    channels: _communities_pb2.Channels
    messages: _messages_pb2.Messages
    relationships: _friends_pb2.Relationships
    chats: _chats_pb2.Chats
    file_part: _media_pb2.FilePart
    created_invite: _auth_pb2.CreatedInvite
    member_list: _communities_pb2.MemberList
    initialized: Initialized
    chat: _chats_pb2.Chat
    community_roles: _communities_pb2.CommunityRoles
    channel_override: _communities_pb2.ChannelOverride
    channel_overrides: _communities_pb2.ChannelOverrides
    sessions: _auth_pb2.Sessions
    user_details: _users_pb2.UserDetails
    removed_members: _communities_pb2.RemovedMembers
    group: _types_pb2.Group
    invite_preview: _auth_pb2.InvitePreview
    room_info: _voice_pb2.RoomInfo
    media_embed: _media_pb2.MediaEmbed
    profile: _users_pb2.Profile
    invite_list: _auth_pb2.InviteList
    saved_stickers: _stickers_pb2.SavedStickers
    files: _media_pb2.Files
    sticker_pack: _stickers_pb2.StickerPack
    payment_link: _billing_pb2.PaymentLink
    account: _settings_pb2.Account
    members: _communities_pb2.Members
    community_settings: _communities_pb2.CommunitySettings
    subscription: _billing_pb2.Subscription
    totp: _settings_pb2.Totp
    unread_mentions: _messages_pb2.UnreadMentions
    discovery_communities: _discovery_pb2.DiscoveryCommunities
    room_states: _communities_pb2.RoomStates
    user_settings: _settings_pb2.UserSettings
    def __init__(self, req_id: _Optional[int] = ..., trace_id: _Optional[str] = ..., error: _Optional[_Union[RPCError, _Mapping]] = ..., sent_message: _Optional[_Union[_messages_pb2.SentMessage, _Mapping]] = ..., authorization: _Optional[_Union[_auth_pb2.Authorization, _Mapping]] = ..., communities: _Optional[_Union[_communities_pb2.Communities, _Mapping]] = ..., channels: _Optional[_Union[_communities_pb2.Channels, _Mapping]] = ..., messages: _Optional[_Union[_messages_pb2.Messages, _Mapping]] = ..., relationships: _Optional[_Union[_friends_pb2.Relationships, _Mapping]] = ..., chats: _Optional[_Union[_chats_pb2.Chats, _Mapping]] = ..., file_part: _Optional[_Union[_media_pb2.FilePart, _Mapping]] = ..., created_invite: _Optional[_Union[_auth_pb2.CreatedInvite, _Mapping]] = ..., member_list: _Optional[_Union[_communities_pb2.MemberList, _Mapping]] = ..., initialized: _Optional[_Union[Initialized, _Mapping]] = ..., chat: _Optional[_Union[_chats_pb2.Chat, _Mapping]] = ..., community_roles: _Optional[_Union[_communities_pb2.CommunityRoles, _Mapping]] = ..., channel_override: _Optional[_Union[_communities_pb2.ChannelOverride, _Mapping]] = ..., channel_overrides: _Optional[_Union[_communities_pb2.ChannelOverrides, _Mapping]] = ..., sessions: _Optional[_Union[_auth_pb2.Sessions, _Mapping]] = ..., user_details: _Optional[_Union[_users_pb2.UserDetails, _Mapping]] = ..., removed_members: _Optional[_Union[_communities_pb2.RemovedMembers, _Mapping]] = ..., group: _Optional[_Union[_types_pb2.Group, _Mapping]] = ..., invite_preview: _Optional[_Union[_auth_pb2.InvitePreview, _Mapping]] = ..., room_info: _Optional[_Union[_voice_pb2.RoomInfo, _Mapping]] = ..., media_embed: _Optional[_Union[_media_pb2.MediaEmbed, _Mapping]] = ..., profile: _Optional[_Union[_users_pb2.Profile, _Mapping]] = ..., invite_list: _Optional[_Union[_auth_pb2.InviteList, _Mapping]] = ..., saved_stickers: _Optional[_Union[_stickers_pb2.SavedStickers, _Mapping]] = ..., files: _Optional[_Union[_media_pb2.Files, _Mapping]] = ..., sticker_pack: _Optional[_Union[_stickers_pb2.StickerPack, _Mapping]] = ..., payment_link: _Optional[_Union[_billing_pb2.PaymentLink, _Mapping]] = ..., account: _Optional[_Union[_settings_pb2.Account, _Mapping]] = ..., members: _Optional[_Union[_communities_pb2.Members, _Mapping]] = ..., community_settings: _Optional[_Union[_communities_pb2.CommunitySettings, _Mapping]] = ..., subscription: _Optional[_Union[_billing_pb2.Subscription, _Mapping]] = ..., totp: _Optional[_Union[_settings_pb2.Totp, _Mapping]] = ..., unread_mentions: _Optional[_Union[_messages_pb2.UnreadMentions, _Mapping]] = ..., discovery_communities: _Optional[_Union[_discovery_pb2.DiscoveryCommunities, _Mapping]] = ..., room_states: _Optional[_Union[_communities_pb2.RoomStates, _Mapping]] = ..., user_settings: _Optional[_Union[_settings_pb2.UserSettings, _Mapping]] = ...) -> None: ...

class RPCError(_message.Message):
    __slots__ = ("error_code", "error_message")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    error_message: str
    def __init__(self, error_code: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class Initialize(_message.Message):
    __slots__ = ("client_id", "device_type", "device_version", "app_version", "no_subscribe")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    NO_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    device_type: str
    device_version: str
    app_version: str
    no_subscribe: bool
    def __init__(self, client_id: _Optional[int] = ..., device_type: _Optional[str] = ..., device_version: _Optional[str] = ..., app_version: _Optional[str] = ..., no_subscribe: _Optional[bool] = ...) -> None: ...

class Initialized(_message.Message):
    __slots__ = ("entrypoints", "vapid_public_key")
    ENTRYPOINTS_FIELD_NUMBER: _ClassVar[int]
    VAPID_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    entrypoints: Entrypoints
    vapid_public_key: str
    def __init__(self, entrypoints: _Optional[_Union[Entrypoints, _Mapping]] = ..., vapid_public_key: _Optional[str] = ...) -> None: ...

class Entrypoints(_message.Message):
    __slots__ = ("entrypoints",)
    ENTRYPOINTS_FIELD_NUMBER: _ClassVar[int]
    entrypoints: _containers.RepeatedCompositeFieldContainer[_types_pb2.Entrypoint]
    def __init__(self, entrypoints: _Optional[_Iterable[_Union[_types_pb2.Entrypoint, _Mapping]]] = ...) -> None: ...
