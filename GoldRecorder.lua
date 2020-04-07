local frame = CreateFrame("Frame")
frame:RegisterEvent("ADDON_LOADED")
frame:RegisterEvent("PLAYER_LOGOUT")

frame:SetScript("OnEvent",function(self,event,...)	
    if (event == "ADDON_LOADED") then		
        local addon = ...
        money = GetMoney()
        realmName = GetRealmName()
        faction = UnitFactionGroup("player")
        characterName = UnitName("player")

        updateTable(realmName, faction, characterName, money)

    end
end)

function updateTable(realmName, faction, characterName, money)
  GoldRecorderDB["@" .. realmName .. "-" .. faction .. "::" .. characterName] = money
end
