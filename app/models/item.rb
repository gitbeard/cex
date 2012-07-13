class Item < ActiveRecord::Base
  attr_accessible :alt_item_number, :item_description, :part_length, :part_number
  
  has_many :daily_inventory
end
