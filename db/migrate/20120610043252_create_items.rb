class CreateItems < ActiveRecord::Migration
  def change
    create_table :items do |t|
      t.string :alt_item_number
      t.string :item_description
      t.string :part_number
      t.string :part_length

      t.timestamps
    end
  end
end
