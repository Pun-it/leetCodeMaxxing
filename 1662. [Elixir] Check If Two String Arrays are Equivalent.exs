defmodule Solution do
  @spec array_strings_are_equal(word1 :: [String.t], word2 :: [String.t]) :: boolean
  def array_strings_are_equal(word1, word2) do
    joiner = ""
    (Enum.join(word1, joiner) === Enum.join(word2,joiner))
  end
end