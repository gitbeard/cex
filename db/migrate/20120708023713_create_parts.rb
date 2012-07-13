class CreateParts < ActiveRecord::Migration
  def change
    create_table :parts do |t|
      t.string :part_number
      t.string :description
      t.integer :column
      t.string :column_header
      t.string :column_color

      t.timestamps
    end
  end
end
