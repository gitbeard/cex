class CreateDailyInventories < ActiveRecord::Migration
  def change
    create_table :daily_inventories do |t|
      t.integer :item_number
      t.integer :location_id
      t.datetime :datetime
      t.integer :quantity
      t.integer :file_id

      t.timestamps
    end
  end
end
